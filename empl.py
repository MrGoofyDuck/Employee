from datetime import datetime
import sqlite3

class Employee:
    def __init__(self, id=None, name=None, position=None, salary=None, hire_date=None):
        self.id = id
        self.name = name
        self.position = position 
        self.salary = salary
        self.hire_date = hire_date

    def get_id(self):
        return self.id
    
    def set_id(self, id:int):
        self.id = id

    def get_name(self):
        return self.name
    
    def set_name(self, name:str):
        self.name = name

    def get_position(self):
        return self.position 
    
    def set_position(self, position:str):
        self.position = position

    def get_salary(self):
        return self.salary
    
    def set_salary(self, salary:float):
        self.salary = salary

    def get_hire_date(self):
        return self.hire_date
    
    def set_hire_date(self, hire_date:float):
        self.hire_date = hire_date

    def __str__(self):
        return f"Employee(id={self.id}, name={self.name}, position={self.position}, salary={self.salary}, hire_date={self.hire_date})"

        
