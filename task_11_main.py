from abc import ABC, abstractmethod

class Calc_interface(ABC):
    @abstractmethod
    def add(self, arg1, arg2):
        raise NotImplemented
    @abstractmethod
    def substract(self,arg1, arg2):
        raise NotImplemented

from 

class Calculator(Calc_interface):
    def add(self, arg1, arg2):
        return arg1 + arg2
    def substract(self,arg1, arg2):
        return  arg1 - arg2
