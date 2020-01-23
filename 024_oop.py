# What is OOP?
# Object oriented programming is a method of programming 
# that attempts to model some process or thing in the world as a class or object.

# What is class?
# class - a blueprint for objects. 
# Classes can contain methods (functions) and attributes (similar to keys in a dict).

# instance - objects that are constructed from a class blueprint 
# that contain their class's methods and properties.

#  __init__ 
# it gets called every time you create an instance of the class (instantiate).
# two underlines on both side of init

# __repr__
# providing a nicer string representation

# self & cls

# @classmethod

# Inheritance
# A key feature of OOP is the ability to define a class which inherits from another class (a "base" or "parent" class).
# In Python, inheritance works by passing the parent class as an argument to the definition of a child class

# super()
# allows us to call the __init__ function of a parent class
# def __init__(self, ...):
# super().__init__(...)

# polymorphism
# An object can take on many forms
# application 1: the same class method works in a similar way for different classes。
# eg: cat.speak()
#     dog.speak()
#     human.speak()
# application 2: the same operation works for different kinds of objects
# eg: sample_list = [1,2,3]
#     sample_tuple = (1,2,3)
#	  sample_string = "awesome"


# Eg 1: Creating a Class 
class Vehicle:

    def __init__(self, make, model, year): 
        # The self keyword refers to the current class instance.
        # self must always be the first parameter to __init__ and any methods and properties on class instances.
        self.make = make
        self.model = model
        self.year = year

#Creating an object that is an instance of a class is called instantiating a class.
# In this case, v becomes a Honda Civic, a new instance of Vehicle
v = Vehicle("Honda", "Civic", 2017) 
v 
# <__main__.Vehicle at 0x10472f5c0>
v.make
# 'Honda'
v.model
# 'Civic'
v.year
# 2017

# Eg 2: Social Media Comment Class
class Comment():
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


# Eg 3: Adding Instance Methods
# A User class with both instance attributes and instance methods
class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(user1.likes("Ice Cream"))
print(user2.likes("Chips"))

print(user2.initials())
print(user1.initials())

print(user2.is_senior()) # return True or False
print(user1.age) #Print age before we update it
print(user1.birthday()) #updates age
print(user1.age) #Print new value of age



#== Class Methods ==

# @classmethod
# A User class with both instance attributes and instance methods

# Ex: basic one

class User2:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User2.active_users += 1

	def logout(self):
		User2.active_users -= 1
		return f"{self.first} has logged out"


# user1 = User2("Joe", "Smith", 68)
# user2 = User2("Blanca", "Lopez", 41)
# print(User2.display_active_users()) # 2
# user1 = User2("Joe", "Smith", 68)
# user2 = User2("Blanca", "Lopez", 41)
# print(User2.display_active_users()) # 4



#==== Inheritance =====

# Ex 1: 

class Animal:
	cool = True

	def make_sound(self, sound):
		print(f"this animal says {sound}")

# Cat class inherits from Animal
class Cat(Animal):
	pass

# Make a new cat instance
blue = Cat()

# Because of inheritance, a Cat has access to:
blue.make_sound("Meow")
print(blue.cool)

#blue is both a Cat and Animal (and base object)
print(isinstance(blue, Cat)) # True
print(isinstance(blue, Animal)) # True
print(isinstance(blue, object)) # True


# Ex 2: super()
# Inheritance Example Using Super()

# OUR "MODEL" FOR ANIMAL AND CAT
# Animal
# 	species
# 	name

# Cat
# 	species
# 	name
# 	breed
# 	favorite_toy


class Animal2:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat2(Animal2): # state the parent class
	def __init__(self, name, breed, toy):
		# super()
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


blue = Cat2("Blue","Scottish Fold", "String")
blue.play()



# Ex 3: Magic Methods
from copy import copy
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		
	def __repr__(self):
		return f"Human named {self.first} {self.last} aged {self.age}"

	def __len__(self):
		return self.age

	def __add__(self, other):
		# When you add two humans together...you get a newborn baby Human!
		if isinstance(other, Human):
			return Human(first='Newborn', last=self.last, age=0)
		return "You can't add that!"

	def __mul__(self, other):
		# When you multiply a Human by an int, you get clones of that Human!
		if isinstance(other, int):
			return [copy(self) for i in range(other)]
			# copy() 
		return "CANT MULTIPLY!"
	


j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)
# print(j)
# print(len(j))
# triplets = j * 3

# kevin and jessica have triplets!
triplets = (k + j) * 3
print(triplets)