from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from PIL import Image
from io import BytesIO
from collections import Counter

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html", name_of_file=None, colors=None)


@app.route("/upload", methods=["POST"])
def upload_image():
    if request.method == "POST":
        # Fetch the data from form
        json_data = {
            "image_bytes": request.files["imgFile"].read(),
            "name_of_file": request.files["imgFile"].filename,
            "num_results": int(request.form.get("num_results")),
            # "date_uploaded": str(datetime.now()).split(".")[0]
        }
        # Save images that was uploaded
        with open(f"uploaded_images/{json_data['name_of_file']}", "wb") as f:
            f.write(json_data['image_bytes'])

        # Pass image data to process colors
        colors = extract_colors(json_data)
        return render_template("index.html", name_of_file=json_data["name_of_file"], colors=colors)


def extract_colors(data: dict) -> list:
    # Open the image from bytes
    image = Image.open(BytesIO(data['image_bytes']))
    print(image.getdata())
    # Resize the image for faster processing
    image = image.resize((150, 150))  # Reduce size for performance
    pass


if __name__ == "__main__":
    app.run(debug=True)
