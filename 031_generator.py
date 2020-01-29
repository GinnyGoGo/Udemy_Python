# 1. Functions vs Generator Functions
# Functions	| Generator Functions
# uses return |	uses yield
# returns once | can yield multiple times
# When invoked, returns the return value | When invoked, returns a generator

def count_up_to(max):
    count = 1
    while count <=max:
        yield count # return the value of count and wait
        count +=1

count_up_to(5) # return a generator object

counter = count_up_to(5) 
next(counter) # each time value 

list(counter) # [1,2,3,4,5]

for num in counter: # get all at one time
    print(num) 
# 1
# 2
# ...