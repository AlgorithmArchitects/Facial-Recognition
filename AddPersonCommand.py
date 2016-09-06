import ICommand

class AddPersonCommand(ICommand):
    @staticmethod
    def name():
        return "AddPerson"
    
    @staticmethod
    def description():
        return "Adds a person to the database given three arguments: ID Number, Name, and the file path of their image."
    
    @staticmethod
    def performCommand(argumentList, openCrWrapper):
        raise NotImplementedError