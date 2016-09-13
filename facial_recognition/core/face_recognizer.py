#!/usr/bin/python
from facial_recognition.constants import INCLUDES_DIRECTORY

import cv2, os
import numpy as np
from PIL import Image

# For face detection we will use the Haar Cascade provided by OpenCV.
CASCADE_PATH = os.path.join(INCLUDES_DIRECTORY, 'haarcascade_frontalface_default.xml')
FACE_CASCADE = cv2.CascadeClassifier(CASCADE_PATH)

# For face recognition we will the the LBPH Face Recognizer
RECOGNIZER = cv2.createLBPHFaceRecognizer()


def get_images_and_labels(path):
    # Id's will be used as labels
    ids = [id for id in os.listdir(path) if not id.endswith(".sh")]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for id in ids:
        student_folder = os.path.join(path, id)
        image_paths = [os.path.join(student_folder, f) for f in os.listdir(student_folder)]
        for image_path in image_paths:
            # Read the image and convert to grayscale
            image_pil = Image.open(image_path).convert('L')
            # Convert the image format into numpy array
            image = np.array(image_pil, 'uint8')
            # Detect the face in the image
            faces = FACE_CASCADE.detectMultiScale(
                image,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            # If face is detected, append the face to images and the label to labels
            for (x, y, w, h) in faces:
                images.append(image[y: y + h, x: x + w])
                labels.append(int(id))
                cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
                cv2.waitKey(1)
        # return the images list and labels list
    return images, labels
