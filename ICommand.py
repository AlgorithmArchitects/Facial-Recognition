from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def name():
        raise NotImplementedError
    
    @staticmethod
    @abstractmethod
    def description():
        raise NotImplementedError
    
    @staticmethod
    @abstractmethod
    def performCommand(argumentList, openCrWrapper):
        raise NotImplementedError