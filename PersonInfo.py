from pip._vendor.pyparsing import basestring
class PersonInfo:
    id_number = ""
    name = ""
    image_file_path = ""
    
    def __init__(self, id_number, name, image_file_path):
        if not isinstance(id_number, basestring)\
        	and not isinstance(name, basestring)\
        	and not isinstance(image_file_path, basestring):
            raise TypeError("Non-string argument.")
        if (not id_number) or (not image_file_path):
            raise ValueError("Missing argument.")
        
        self.id_number = id_number
        self.name = name
        self.image_file_path = image_file_path
