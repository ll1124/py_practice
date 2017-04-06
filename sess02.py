
#
# Author        : ...
# Contact       : ...
# Started on    : 20170322(yyyymmdd)
# Last modified : 20170327(yyyymmdd)
# Project       : ...
#############################################################################
# FUNCTION
# A function is a set of operations in
"""
def power(base, power):
	return base ** power

prnt = power(3,4)
print(prnt)
"""

# A "header"
# cf. any line which ends with ":" is a header in Python
# We define "parameters" inside of a function scope. For now parameters are of
# empty values.
# We put "arguments" into a function, so that the parameters can now have
# actual values.
# cf. It is also possible to define a function without argument


# ... and a "body", which contains the actual operation of things
# Python doesn't require a function to return something.



# There are in large two types of functions. One of them is called the
# "built-in functions" Built-in functions are the functions supported by the
# language itself. It does not require definition of a function. So far, we
# have learnt some built-in functions such as:
# print(), which prints the argument in a human readable form

# len(), which returns the length of the iterable argument



# It is possible to define some functions with built-in names, hence,
# overriding built-in functions - of course not recommended
"""
def len(iterable):
	return "It no longer returns the length of an interable"
prnt = len([0,1,2,3,4])
print(prnt)
"""

# default arguments


#############################################################################
# METHOD
# A method is a function attached to some objects and receives that object as # its first argument

# Some methods for list
"""
someList = ["Example", "for", "Method", "for", "You"]
print(someList)
"""

# append()method adds an element at the end of the list
"""
someList.append("new element")
print(someList)
"""

# pop()method returns
# By default it pops out the last element
"""
prnt = someList.pop()
print(prnt)
print(someList)
"""

# count()method returns the number of how many times an argument appears in
# the list
"""
prnt = someList.count("for")
print(prnt)
prnt = someList.count("Example")
print(prnt)
"""

#############################################################################
# OPTIONAL: MUTABLES AND IMMUTABLES
# For example, lists are immutables
"""
list0 = ["L","I","S","T"]
list1 = list0
print(list0)
print(list1, "\n")
list0.append("E")
print(list0)
print(list1, "\n")
list0 = ["L","E","A","S","T"]
print(list0)
print(list1, "\n")
"""

# ... whereas strs are mutables.
"""
str0 = "orginal str"
str1 = str0
print(str0)
print(str1)
str0 = "new str"
print(str0)
print(str1)
"""

#############################################################################
# INPUT
"""
yourname = input("ENTER YOUR NAME: ")
print()
print("Once upon a time, there was a programmer called...")
print(yourname, "the nerd.")
yourname = input("PRESS ANY KEY TO QUIT")
"""
