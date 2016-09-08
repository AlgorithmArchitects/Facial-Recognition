import ICommand
from argparse import ArgumentError
class RecognizePersonCommand(ICommand):
    @staticmethod
    def name():
        return "RecognizePerson"
    
    @staticmethod
    def description():
        return "Takes an image file path as an argument and attempts to recognize the person in the image."
    
    @staticmethod
    def perform_command(argumentList, openCrWrapper):
        if not isinstance(argumentList, collections.Sequence):
            raise TypeError
        if argumentList.length != 1:
            raise ArgumentError("Wrong number of arguments.")
        if not isinstance(argumentList[0], basestring):
            raise TypeError("Non-string argument.")
        if not os.path.isfile(argumentList[0]):
            raise FileNotFoundError("Given image file does not exist.")
        
        return openCrWrapper.get_person_from_image_file_path(argumentList[0]);