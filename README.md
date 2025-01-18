# Image Color Palette Extractor

This is a web application built with Flask that allows users to upload an image and extract its dominant colors using a k-means clustering algorithm. It provides a simple and intuitive way to identify the primary colors in any image.

## Features

•   **Image Upload:** Allows users to upload images from their local machine.
•   **Dominant Color Extraction:** Uses k-means clustering from scikit-learn to extract a user-specified number of dominant colors from the uploaded image.
•   **Color Display:** Presents the extracted colors as color swatches and displays the corresponding hex color codes.

## Technologies Used

•   **Python:** The primary programming language.
•   **Flask:** A micro web framework for building the web application.
•   **Pillow (PIL):** Used for image loading, manipulation, and resizing.
•   **NumPy:** Used for efficient numerical operations on image data.
•   **scikit-learn (sklearn):**  Used for k-means clustering to extract the dominant colors.
•   **Git:** Used for version control.
•   **HTML/CSS:** Used for creating a basic user interface.
•   **Bootstrap Framework:** Used for making a website look user-fiendly

## Setup and Installation

1.  **Clone the repository:**
   ```bash
  git clone https://github.com/DavlatSTAR/PaletteFinder.git
  ```
3.  **In Terminal run:**
   ```powershell
   pip install -r requrements.txt
   ```
5. **Run main.py**
