#!/usr/bin/python
from facial_recognition.core.face_recognizer import (RECOGNIZER, FACE_CASCADE,
                                                    get_images_and_labels)
from facial_recognition.core.person_info import get_person_info

import click
import cv2
import numpy as np

@click.argument('path')
@click.command()
def recognize(path):
    # TODO: Remove training part, deserialize instead.
    # Call the get_images_and_labels function and get the face images and the
    # corresponding labels
    images, labels = get_images_and_labels(path)
    cv2.destroyAllWindows()

    # Perform the tranining
    RECOGNIZER.train(images, np.array(labels))


    video_capture = cv2.VideoCapture(0)

    with get_person_info() as people:
        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = FACE_CASCADE.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                nbr_predicted, conf = RECOGNIZER.predict(gray[y: y + h, x: x + w])
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                try:
                    person = people.get(nbr_predicted)
                    print("{} is recognized with confidence {}"\
                          .format(person['name'], conf))
                except KeyError:
                    print "Id {} is recognized with confidence {}, but no person information exists"\
                          .format(nbr_predicted, conf)
            # Display the resulting frame
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
