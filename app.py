# app.py (Flask backend)
from flask import Flask, render_template, request, jsonify
import os
from PIL import Image
import pdfToImage
import textExtract

app = Flask(__name__)



# API endpoint to handle file uploads and data extraction
@app.route('/uploadPdf', methods=['POST'])
def uploadPdf():
    # Get the uploaded file
    uploaded_file = request.files['filePdf']

    # Save the file to a temporary location
    file_path = 'temp.pdf'
    uploaded_file.save(file_path)

    # Extract text from PDF or image
    if file_path.lower().endswith('.pdf'):
        imgPath = pdfToImage.pdfToImage(file_path)
        text = textExtract.extract_text_from_coordinates(imgPath)
    else:
        text = textExtract.extract_text_from_coordinates(file_path)

    # print(text)

    # Delete the temporary file
    os.remove(file_path)

    # Return the extracted data as a JSON response
    return jsonify(text)


@app.route('/uploadImage', methods=['POST'])
def uploadImage():
    # Get the uploaded file
    uploaded_file = request.files['fileImage']

    # Save the file to a temporary location
    file_path = 'temp.jpg'
    uploaded_file.save(file_path)

    # Extract text from PDF or image
    if file_path.lower().endswith('.jpg'):
        text = textExtract.extract_text_from_coordinates(file_path)
    else:
        imgPath = pdfToImage.pdfToImage(file_path)
        text = textExtract.extract_text_from_coordinates(imgPath)

    # print(text)

    # Delete the temporary file
    os.remove(file_path)

    # Return the extracted data as a JSON response
    return jsonify(text)

# Render the homepage
@app.route('/')
def index():
    return render_template('./index.html')

if __name__ == '__main__':
    app.run(debug=False)
