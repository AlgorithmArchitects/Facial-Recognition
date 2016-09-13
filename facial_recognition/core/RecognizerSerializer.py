import os
from facial_recognition import constants
import cv2

SAVE_PATH = os.path.join(constants.USER_DATA_DIRECTORY, "csv_recognizer_info.rec")

class RecognizerSerializer():

    @staticmethod
    def deserialize_recognizer():
        if os.path.isfile(SAVE_PATH):
            RECOGNIZER = cv2.createLBPHFaceRecognizer()
            return RECOGNIZER.load(SAVE_PATH)
        else:
            raise os.FileNotFoundError

    @staticmethod
    def serialize_recognizer(recognizer):
        recognizer.save(SAVE_PATH)