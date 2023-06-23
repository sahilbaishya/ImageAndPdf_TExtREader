# import module
from pdf2image import convert_from_path
import os

def pdfToImage(pdf_path):
    images = convert_from_path(pdf_path)
    images[0].save('temp.jpg', 'JPEG')
    image_path = os.path.relpath('temp.jpg', '.')
    return image_path
 
 
# Store Pdf with convert_from_path function
# images = convert_from_path('sample1.pdf')

# output_folder = "output_images"
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

 
# for i in range(len(images)):
   
#       # Save pages as images in the pdf
#     images[i].save(os.path.join(output_folder, 'page'+ str(i) +'.jpg'), 'JPEG')

# images[0].save('temp.jpg', 'JPEG')

# image_path = os.path.relpath('temp.jpg', '.')

