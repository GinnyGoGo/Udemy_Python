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
