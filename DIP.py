#Dependency inversion
class FrontEnd:
     def __init__(self, back_end):
         self.back_end = back_end
     def display_data(self):
         data = self.back_end.get_data_from_database()
         print("Display data:", data)
class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"
    
    
    
#this code solve using DIP   
from abc import ABC, abstractmethod


class DataService(ABC):
    @abstractmethod
    def get_data(self):
        pass


class BackEnd(DataService):
    def get_data(self):
        return "Data from the database"

class FrontEnd:
    def __init__(self, data_service: DataService):
        self.data_service = data_service

    def display_data(self):
        data = self.data_service.get_data()
        print("Display data:", data)


back_end = BackEnd()
front_end = FrontEnd(back_end)
front_end.display_data()
