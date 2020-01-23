# ====== Part 1 ========

# A User class with class attributes 

class User:

    # initial active user value = 0
	active_users = 0

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
        # plus one everytime when a new user was created
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

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


# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))

# print(user2.initials())
# print(user1.initials())

# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)
# user1.say_hi()

print(User.active_users) 
# 0
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.active_users)
# 2
print(user2.logout())
print(User.active_users)
# 1




# ====== Part 2 ========

# A User class with class methods
# using @classmethod and cls

class User2:
	active_users = 0

    # NEW CODE
	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))
    # NEW CODE

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User2.active_users += 1

	def logout(self):
		User2.active_users -= 1
		return f"{self.first} has logged out"

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



# user1 = User2("Joe", "Smith", 68)
# user2 = User2("Blanca", "Lopez", 41)
# print(User2.display_active_users())
# user1 = User2("Joe", "Smith", 68)
# user2 = User2("Blanca", "Lopez", 41)
# print(User2.display_active_users())

tom = User2.from_string("Tom,Jones,89")
print(tom.first)
print(tom.full_name())
print(tom.birthday())



# ====== Part 3 ========

# A User class with string representation

 class User3:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User3.active_users += 1

	# NEW CODE
	def __repr__(self):
		return f"{self.first} is {self.age}"
	# NEW CODE

	def logout(self):
		User3.active_users -= 1
		return f"{self.first} has logged out"

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


tom = User3.from_string("Tom,Jones,89")

j = User3("judy", "steele", 18)
j = str(j)
print(j) # judy is 18


