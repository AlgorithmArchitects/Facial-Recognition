import ICommand
class RecognizePersonCommand(ICommand):
    @staticmethod
    def name():
        return "RecognizePerson"
    
    @staticmethod
    def description():
        return "Takes an image file path as an argument and attempts to recognize the person in the image."
    
    @staticmethod
    def performCommand(argumentList, openCrWrapper):
        raise NotImplementedError