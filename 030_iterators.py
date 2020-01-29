# __iter__() should return a iterator 

# Eg: 

# 1) Basic

def my_for(iterable):
	iterator = iter(iterable)
	print(next(iterator))
	print(next(iterator))

my_for("hello") 
# h 
# e 

# 2) Custom For Loop

def my_for2(iterable):
	iterator = iter(iterable)
	while True:
		try:
			print(next(iterator))
		except StopIteration:
			print("END OF ITERATOR!")
			break

my_for2("hello") 
# h 
# e 
# l 
# l 
# o  
# END OF ITERATOR!


# 3) custome function
# for num in [1,2,3]
# for char in "hi there"

def my_for3(iterable, func):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			break
		else:
			func(thing)
		
def square(x):
	print(x*x)

my_for3("lol", print) 
# l 
# o 
# l
my_for3([1,2,3], square) 
# 1
# 4
# 9


# Eg: Custom Iterator
class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration


for x in Counter(50,70):
	print(x)
