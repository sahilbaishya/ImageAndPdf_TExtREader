import cv2
import pytesseract

def textMarker (image_path):
    image = cv2.imread(image_path)

# Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform text detection using OCR (Tesseract)
    config = r'--oem 3 --psm 6'  # OCR engine configuration
    text = pytesseract.image_to_data(gray, config=config)

# Process the text detection results
    lines = text.split('\n')[1:]  # Skip the header line
    textRegions = []

    text_coordinates = []

    for line in lines:
        data = line.split('\t')
        if len(data) == 12:
            x, y, w, h = int(data[6]), int(data[7]), int(data[8]), int(data[9])
            conf = int(data[10])

        # Filter out regions with low confidence or non-textual content
            if conf > 60 and data[11].strip() != '':
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text_coordinates.append((x, y, x+w, y+h))

    # print(text_coordinates)
    # cv2.imshow('Image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return text_coordinates, image


