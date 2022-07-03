class Nikola:
	__slots__ = ['name', 'age']
 
	def __init__(self, name, age):
		self.name = name
		self.age = age
		if self.name !='Николай':
        		self.name = f'Я не {self.name}, а Николай'

 
 

person1 = Nikola('Виталий', 33)
person2 = Nikola('Николай', 25)
print(person1.name)
print(person2.name)
person2.surname = 'Владимирович'