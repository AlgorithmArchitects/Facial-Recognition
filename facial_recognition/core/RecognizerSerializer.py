import pickle
import constants
import os
import dill
class RecognizerSerializer():
    @staticmethod
    def deserialize_recognizer():
        if(os.path.isfile(constants.USER_DATA_DIRECTORY + "\\csv_recognizer_info")):
            return dill.load(open(constants.USER_DATA_DIRECTORY + "\\csv_recognizer_info", "rb"))
        else:
            raise FileNotFoundError
    
    @staticmethod
    def serialize_recognizer(recognizer):
        dill.dump(recognizer, open(constants.USER_DATA_DIRECTORY + "\\csv_recognizer_info", "wb"))