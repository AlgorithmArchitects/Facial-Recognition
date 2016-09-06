from pip._vendor.pyparsing import basestring
class PersonInfo:
    id_number = ""
    name = ""
    imageFilePath = ""
    
    def __init__(self, idNumber, name, imageFilePath):
        if not isinstance(idNumber, basestring)\
        	and not isinstance(name, basestring)\
        	and not isinstance(imageFilePath, basestring):
            raise TypeError
        if (not idNumber) or (not imageFilePath):
            raise ValueError
        
        self.idNumber = idNumber
        self.name = name
        self.imageFilePath = imageFilePath
