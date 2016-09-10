import pickle
class RecognizerSerializer():
    @staticmethod
    def deserialize_recognizer():
        if(os.path.isfile("C:/csv_recognizer_info")):
            return pickle.load(open("C:/csv_recognizer_info", "rb"))
        else:
            raise FileNotFoundError
    
    @staticmethod
    def serialize_recognizer(recognizer):
        pickle.dump(recognizer, open("C:/csv_recognizer_info", "wb"))