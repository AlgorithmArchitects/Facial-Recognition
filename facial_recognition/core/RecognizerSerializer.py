import pickle
from .. import constants
import os

class RecognizerSerializer():
    @staticmethod
    def deserialize_recognizer():
        if(os.path.isfile(constants.USER_DATA_DIRECTORY + "\\csv_recognizer_info.rec")):
            return pickle.load(open(constants.USER_DATA_DIRECTORY + "\\csv_recognizer_info", "rb"))
        else:
            raise os.FileNotFoundError
    
    @staticmethod
    def serialize_recognizer(recognizer):
        pickle.dump(recognizer, open(constants.USER_DATA_DIRECTORY + "\\csv_recognizer_info.rec", "wb"))
