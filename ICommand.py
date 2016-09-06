import abc

class ICommand(object):
	__metaclass__ = abc.ABCMeta
	@staticmethod
	@abc.abstractmethod
	def name():
		raise NotImplementedError
	
	@staticmethod
	@abc.abstractmethod
	def description():
		raise NotImplementedError
	
	@staticmethod
	@abc.abstractmethod
	def performCommand(argumentList, openCrWrapper):
		raise NotImplementedError
