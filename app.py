from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from main import do

app = Flask(__name__)

# Mock function to process the file
def do_smth(file_input):
    # Dummy logic: assume success if the filename contains "success"
    if "success" in file_input.filename:
        return "success"
    return "fraud"

# Upload folder (temporary)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file_input")
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            file.save(filepath)
            result = do(filepath)
            return redirect(url_for("result", status=result))
    return render_template("index.html")

@app.route("/result")
def result():
    status = request.args.get("status")
    return render_template("results.html", status=status)

if __name__ == "__main__":
    app.run(debug=True)
