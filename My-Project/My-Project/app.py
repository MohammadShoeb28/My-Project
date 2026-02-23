from flask import Flask, render_template, request
import os
import whisper
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load whisper model
model = whisper.load_model("base")

# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/speech")
def speech():
    return render_template("speech.html", transcription="")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/about")
def about():
    return render_template("about.html")

# ---------- TRANSCRIBE ----------
@app.route("/transcribe", methods=["POST"])
def transcribe():

    file = request.files["audio"]
    filename = secure_filename(file.filename)

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    result = model.transcribe(
        audio=filepath,
        language="hi",
        task="translate"
    )

    return render_template(
        "speech.html",
        transcription=result["text"]
    )

if __name__ == "__main__":
    app.run(debug=True)