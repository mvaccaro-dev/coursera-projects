import zipfile
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np
import io
import math
import time


"""
-------------------------------------------------------------------
    Loading the face detection classifier
-------------------------------------------------------------------
"""
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

"""
-------------------------------------------------------------------
    Data loaded from the zip file
-------------------------------------------------------------------
"""
zip_data = []


"""
-------------------------------------------------------------------
    Hard-coded dimension for normalization
-------------------------------------------------------------------
"""
thumb_dim = 64


"""
-------------------------------------------------------------------
    Hard-coded images per row
-------------------------------------------------------------------
"""
img_per_row = 5


"""
-------------------------------------------------------------------
    Function to load the data from the zip file
-------------------------------------------------------------------
"""
def load_data(zip_file):
    # DEBUG
    print("[DEBUG] Loading data...")
    start_time = time.time()
    # Load the zipfiles
    with zipfile.ZipFile(zip_file, 'r') as zipImages:
        # Open each image
        for image in zipImages.infolist():
            # Image info
            image_name = image.filename
            image_bytes = zipImages.read(image_name)
            # Process image
            process_data(image_name, image_bytes)            
    # DEBUG
    end_time = time.time()
    elapsed_time = time.strftime("%H:%M:%S", time.gmtime(end_time - start_time))
    print("[DEBUG] Data loaded in {}".format(elapsed_time))


"""
-------------------------------------------------------------------
    Function for the parallel image processing
-------------------------------------------------------------------
"""
def process_data(image_name, image_bytes):
    # Load PIL image from bytes
    image = Image.open(io.BytesIO(image_bytes))
    # Convert PIL image to grayscale
    gray_image = image.convert("L")
    # Convert PIL image to numpy array
    np_image = np.array(gray_image)
    # Detect text with (py)Tesseract
    text = pytesseract.image_to_string(np_image)
    text = text.replace("-\n", "")
    text = text.replace("\n", " ")
    # Detect face boxes with OpenCV
    faces = []
    face_boxes = face_cascade.detectMultiScale(np_image, 1.29, 8)
    for x, y, w, h in face_boxes:
        # Crop original image
        cropped = image.crop((x, y, x + w, y + h))
        # Resize
        resized = cropped.resize((thumb_dim, thumb_dim))
        # Append to the list
        faces.append(resized)
    # Build sheet
    sheet = None
    if len(faces) > 0:
        rows = math.ceil(len(faces) / img_per_row)
        # Build the empty sheet
        sheet = Image.new('RGB', (thumb_dim * img_per_row, thumb_dim * rows))
        # Iterate faces
        x_pos = 0
        y_pos = 0
        for face in faces:
            sheet.paste(face, (x_pos, y_pos))
            x_pos += face.width
            if x_pos >= sheet.width:
                x_pos = 0
                y_pos += face.height
    # Build dictionary
    image_info = { 
        "name": image_name,
        "image": image,
        "text": text,
        "faces": sheet
    }
    zip_data.append(image_info)


"""
-------------------------------------------------------------------
    Function to search the string
-------------------------------------------------------------------
"""
def search_string(word):
    print("----------------------------------------------------------")
    print("Searching for: {}".format(word))
    print("----------------------------------------------------------")
    for data in zip_data:
        if word in data['text']:
            print("Results found in file {}".format(data['name']))
            if data['faces'] is None:
                print("But there were no faces in that file!")
            else:
                display(data['faces'])


"""
-------------------------------------------------------------------
    Main loop
-------------------------------------------------------------------
"""
load_data('readonly/images.zip')        # test with small_img.zip in the repository
search_string('Christopher')
search_string('Mark')


