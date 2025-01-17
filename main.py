from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_image():
    if request.method == "POST":
        # Fetch the data from form
        json_data = {
            "image_bytes": request.files["imgFile"].read(),
            "name_of_file": request.files["imgFile"].filename,
            "num_results": request.form.get("num_results"),
            # "date_uploaded": str(datetime.now()).split(".")[0]
        }
        # Save images that was uploaded
        with open(f"uploaded_images/{json_data['name_of_file']}", "wb") as f:
            f.write(json_data['image_bytes'])

        # Pass image data to process colors
        process_image(json_data)
        return redirect(url_for("index_page"))


def process_image(data: dict):
    pass


if __name__ == "__main__":
    app.run(debug=True)
