import abc

class ICommand(object):
	__metaclass__ = abc.ABCMeta
	@staticmethod
	@abc.abstractmethod
	def name():#returns the name that will be used to recognize the console command
		raise NotImplementedError
	
	@staticmethod
	@abc.abstractmethod
	def description():#returns a string describing function usage
		raise NotImplementedError
	
	@staticmethod
	@abc.abstractmethod
	def performCommand(argumentList, openCrWrapper):#accepts an array of arguments and an OpenCvWrapper and performs the given operation
		raise NotImplementedError
