class Student():
 
    def __init__(self, name = "Ivan", age = 18, groupNumber = "10A"):
 
     self.name = name
     self.age = age
     self.groupNumber = groupNumber
 
    def get_name(self):
        return f'Name of the student is - {self.name}'

    def get_age(self):
        return f'Age of the student is - {self.age}'

    def get_groupNumber (self):
        return f'The groupNumber of the student is - {self.groupNumber}'
    
    def Set_name_age(self, name, age):
        self.name = name
        self.age = age
        return f'Name of the student is - {self.name}, age of the student is - {self.age}'
 
    def set_groupNumber(self,groupNumber):
        self.groupNumber = groupNumber
        return f'The groupNumber of the student is - {self.groupNumber}.'
 
Artem = Student("Artem", 15, "5d")
Elena = Student("Elena", 17, "7a")
Irina = Student("Irina", 16, "10f")
Ivan = Student()
Petr = Student("Petr", 20, "1s")
print(f'{Artem.get_name()}, {Artem.get_age()}, {Artem.get_groupNumber()}')
print(f'Name of the student is - {Ivan.name}, age of the student is - {Ivan.age}, the groupNumber of the student is - {Ivan.groupNumber}.')
print(f'{Irina.Set_name_age("Anna", 30)}, {Petr.set_groupNumber("))2")}')

