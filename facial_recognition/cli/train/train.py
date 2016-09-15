#!/usr/bin/python
from facial_recognition.core.face_recognizer import (RECOGNIZER,
                                                    get_images_and_labels)
from facial_recognition.constants import DEFAULT_PICTURES_DIRECTORY

import click
import cv2
import numpy as np
from ...core import RecognizerSerializer as rs

@click.option('--path', default=DEFAULT_PICTURES_DIRECTORY, help="Pictures directory to train from")
@click.command()
def train(path):
    # Call the get_images_and_labels function and get the face images and the
    # corresponding labels
    images, labels = get_images_and_labels(path)
    cv2.destroyAllWindows()

    # Perform the tranining
    RECOGNIZER.train(images, np.array(labels))

    rs.RecognizerSerializer.serialize_recognizer(RECOGNIZER)
