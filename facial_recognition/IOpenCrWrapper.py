import abc

class IOpenCrWrapper(object):
	__metaclass__ = abc.ABCMeta
	@abc.abstractmethod
	def __init__(self, initFromFilePath):#filepath points to our db info file (if that is what we use)
		pass
	
	@abc.abstractmethod
	def try_add_new_person(self, personInfo):#returns true if added, false otherwise
		pass
	
	@abc.abstractmethod
	def get_person_from_image_file_path(self, imageFilePath):#returns a PersonInfo or None if not found
		pass
