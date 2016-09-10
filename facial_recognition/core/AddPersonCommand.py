from argparse import ArgumentError
class AddPersonCommand(ICommand):
    @staticmethod
    def name():
        return "AddPerson"
    
    @staticmethod
    def description():
        return "Adds a person to the database given three arguments: ID Number, Name, and the file path of their image."
    
    @staticmethod
    def perform_command(argumentList, openCrWrapper):
        if not isinstance(argumentList, collections.Sequence):
            raise TypeError
        if argumentList.length != 3:
            raise ArgumentError("Wrong number of arguments.")
        if not isinstance(argumentList[0], basestring):
            raise TypeError("Non-string argument.")
        if not isinstance(argumentList[1], basestring):
            raise TypeError("Non-string argument.")
        if not isinstance(argumentList[2], basestring):
            raise TypeError("Non-string argument.")
        if not os.path.isfile(argumentList[0]):
            raise FileNotFoundError("Given image file does not exist.")
        
        person_to_add = PersonInfo(argumentList[0], argumentList[1], argumentList[2])
        openCrWrapper.try_add_new_person(person_to_add)