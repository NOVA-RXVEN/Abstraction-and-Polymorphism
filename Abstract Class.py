from abc import ABC, abstractmethod

class AbstractClass(ABC):
    
    def print(self, x):
        print(f"Passed Value: {x}")
        
    @abstractmethod
    def task(self):
        print("We are inside of AbstractClass task")
        
class test_class(AbstractClass):
    
    def task(self):
        print("We are inside test_class task")
        
test_obj = test_class()
test_obj.task()
test_obj.print(1500)