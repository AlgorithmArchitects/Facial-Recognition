#!/usr/bin/python
from facial_recognition.core.face_recognizer import (RECOGNIZER,
                                                    get_images_and_labels)

import click
import cv2
import numpy as np

@click.argument('path')
@click.command()
def train(path):
    # Call the get_images_and_labels function and get the face images and the
    # corresponding labels
    images, labels = get_images_and_labels(path)
    cv2.destroyAllWindows()

    # Perform the tranining
    RECOGNIZER.train(images, np.array(labels))
    # TODO: Serialize trained model
