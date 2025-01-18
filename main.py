from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html", name_of_file=None, colors=None, num_of_results=None)


@app.route("/upload", methods=["POST"])
def upload_image():
    if request.method == "POST":
        # Fetch the data from form
        json_data = {
            "name_of_file": request.files["imgFile"].filename,
            "num_results": int(request.form.get("num_results")),
        }
        # Save images that was uploaded
        with open(f"static/uploaded_images/{json_data['name_of_file']}", "wb") as f:
            f.write(json_data['image_bytes'])

        # Pass image data to process colors
        colors = extract_colors(json_data)
        return render_template("index.html", name_of_file=json_data["name_of_file"], colors=colors, num_of_results=json_data['num_results'])


def extract_colors(data: dict) -> list[tuple]:
    """
    Extracts the most dominant colors from an image using k-means clustering.

    Args:
        data (dict): A dictionary containing the image file name (name_of_file) and num_of_resutls.

    Returns:
        list[tuple]: A list of the dominant colors, where each color
        is a tuple of (Red, Green, Blue) integer values.
    """
    # Open the image from bytes
    image = Image.open(f"static/uploaded_images/{data['name_of_file']}")
    image = image.convert('RGB')
    image_array = np.array(image)

    # Reshape the image into a 2D array of RGB values
    pixels = image_array.reshape(-1, 3)

    kmeans = KMeans(n_clusters=data.get('num_results', 10), random_state=42, n_init='auto')
    kmeans.fit(pixels)

    # Get the cluster centers (dominant colors) and their counts
    dominant_colors = kmeans.cluster_centers_.astype(int)
    counts = Counter(kmeans.labels_)

    # Sort colors by frequency
    sorted_colors = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    top_colors = [tuple(dominant_colors[idx]) for idx, _ in sorted_colors]

    return top_colors


if __name__ == "__main__":
    app.run(debug=True)
