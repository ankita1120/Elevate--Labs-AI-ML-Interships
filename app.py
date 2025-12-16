from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from scoring import rank_resumes
import os
from werkzeug.utils import secure_filename
import time
import pandas as pd
from io import BytesIO

app = Flask(__name__)
app.secret_key = "replace-with-your-secret"  # for flashing messages
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXT = {".pdf", ".txt"}

def allowed(filename):
    return os.path.splitext(filename)[1].lower() in ALLOWED_EXT

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_files():
    # Get files and job description
    files = request.files.getlist("resumes")
    job_desc = request.form.get("job_description", "").strip()

    if not job_desc:
        flash("Please paste a job description.")
        return redirect(url_for("index"))

    if not files or all(f.filename == "" for f in files):
        flash("Please select at least one resume file (PDF or TXT).")
        return redirect(url_for("index"))

    saved_files = []
    for file in files:
        if file and file.filename:
            filename = secure_filename(file.filename)
            if not allowed(filename):
                flash(f"Skipping {filename}: only PDF or TXT allowed.")
                continue
            unique_filename = f"{int(time.time())}_{filename}"
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], unique_filename)
            file.save(filepath)
            saved_files.append(filepath)

    if not saved_files:
        flash("No valid resumes uploaded.")
        return redirect(url_for("index"))

    results = rank_resumes(job_desc, saved_files)

    # Save results in session-like storage by writing to a CSV in memory and sending path via template
    # We'll create the CSV when user clicks download; for now pass 'results' to template
    return render_template("results.html", results=results)

@app.route("/download_report", methods=["POST"])
def download_report():
    # Expect JSON-like form fields: filenames and scores
    # For simplicity, parse posted form fields named file_0, score_0, etc.
    entries = []
    i = 0
    while True:
        fn_key = f"file_{i}"
        sc_key = f"score_{i}"
        if fn_key not in request.form:
            break
        entries.append({
            "file": request.form[fn_key],
            "score": float(request.form.get(sc_key, 0))
        })
        i += 1

    if not entries:
        flash("No report data found.")
        return redirect(url_for("index"))

    df = pd.DataFrame(entries)
    df = df.sort_values(by="score", ascending=False).reset_index(drop=True)

    # Build CSV in memory and return
    buf = BytesIO()
    df.to_csv(buf, index=False)
    buf.seek(0)

    return send_file(
        buf,
        as_attachment=True,
        download_name="resume_ranking_report.csv",
        mimetype="text/csv"
    )

if __name__ == "__main__":
    app.run(debug=True)
