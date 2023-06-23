import textMarker
import pytesseract
import cv2
import matplotlib as plt


# text_coordinates, image = textMarker.textMarker('public/12334.png')

def extract_text_from_coordinates(image_path):
    image = cv2.imread(image_path)
    coordinates, img = textMarker.textMarker(image_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract text from each set of coordinates
    extracted_text = []
    for coord in coordinates:
        x1, y1, x2, y2 = coord
        cropped_image = gray[y1:y2, x1:x2]
        text = pytesseract.image_to_string(cropped_image)
        extracted_text.append(text.strip())

    return extracted_text

# Load the image


# Specify the coordinates of the regions of interest

# Extract text from the specified coordinates
# text = extract_text_from_coordinates("public/12334.png")

# # Print the extracted text
# for i, region_text in enumerate(text):
#     print(region_text + " ")