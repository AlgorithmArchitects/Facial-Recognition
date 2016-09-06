import abc

class IOpenCrWrapper(object):
	__metaclass__ = abc.ABCMeta
	@abc.abstractmethod
	def __init__(self, initFromFilePath):#filepath points to our db info file (if that is what we use)
		pass
	
	@abc.abstractmethod
	def tryAddNewPerson(self, personInfo, imageFilePath):#returns true if added, false otherwise
		pass
	
	@abc.abstractmethod
	def getPersonFromImageFilePath(self, imageFilePath):#returns a PersonInfo or None if not found
		pass
