# -*- coding: utf-8 -*-
# print("Good evening to code!")

#############################################################################
# COMMENTS
# Things like this is called comments, which is not ignored by the parser.

#############################################################################
# VARIABLE
# A variable is a memory with a name which contains some value.

#var = 1
#print(var)
#var = "ninano"
#print(var)
#other_var = var
#print(other_var)
#print(var)

#var = "nenyanyo"
#print(other_var)
#print(var)

# Referencing an undefined variable is illegal
#print(not yet defined)

# cf. Unlike other languages again, Python doesn't have the type const
# (constant)
#############################################################################
# TYPES OF (REALLY SIMPLE) DATA
# int, integer
#prnt = 1
#print()

# float, floats are real (and rational) numbers
# 소수입니다.

# complex, I have never used it in practice.
# 그래서 안 해

# int, float, complex are all numerics, which means they can be operated by some opereators

# str, string
# A str is a series of characters of length from 0 to ... I don't remember.
# A str is defined by entering some characters bewteen " ", "" "",' ','' '',""" """
#prnt = "a string"
#print(prnt)

# Some mechanics for str operation.
# Most of the time you print a str, - unlike some other types - it is printed
# as it is.
#myStr"What you see is what you get"
#print(myStr)

# Sometimes it isn't
# myStr = "\ is a single backslash, \\are two backslashes \\\are triple backslashes"
# print(myStr)

# Commonly used symbols with escape characters
# bs1 ="This is a \n newline" # newline
# bs2 = "This is a \t tab" # tab
# bs3 = "This is a \\ backslash" # backslash
# print(bs1)
# print(bs2)
# print(bs3)

# "\" is called an "escape character" all characters typed bewteen \ and a
# whitespace has a special meaning (if any) when it is written inside of the
# quotation marks

# boolean, True of False
# prnt = 1 == 2
# print(prnt)

# prnt = (1 == 2) or (2 == 2)
# print(prnt)

# cf. Unlike other languages, - e.g. C, JAVA - there's no difference between 1
# length strings and more than 1 length strings. chars and strs are all str in
# Python.
#############################################################################
# TYPES OF (RATHER USEFUL) DATA
# list
# list is the easiest form of "iterables" in Python.
#someList = [2017, 3, 27, 17, 5]
#print(someList)

# lists, more generally, iterables have length.
#prnt = len(someList)

# Some operations with lists
# Indexing, Slicing
#
# pop(), append()
#

# Elements of a list can be of any type - personally not recommended, though.
# prnt = [1, "EE", "Sam", 100]
# print(prnt)

# tuple
#으앙...

# One big difference between lists and tuples is that length of lists can be
# changed whereas that of tuples is not.



# set
# A set is a group of non redundant elements.
# prnt = set([1, 2, 3, 4, 5, 4, 3, 2, 1])
# print(prnt)

# Indexing is not supported for sets.
# prnt = set([1,2,3])[0]
# print(prnt)

# dict, dictionary
# prnt = {"k1":1, "k2":"그만", "k3":["그","만","해"]}
# print(prnt)
# print(prnt["k3"])

#############################################################################
# CONDITIONAL STATEMENTS
# someInt = 10 # Pick an int of your choice
# mod_someInt = someInt % 2
# if mod_someInt == 1: # This part is called a "header"
	# print("someInt is an odd number")
# else:
	# print("someInt is an even number") # This indented part is called a "body"
# cf. Python does not support switch conditional statements

#############################################################################
# for STATEMENTS, while STATEMENTS
# for STATEMENTS
# for ejl in ["너와", "Naui", "연결", "Gori"]:
	# print(ejl)

# while STATEMENTS
# someList = ["Gori", "연결", "Naui", "너와"]
# while len(someList):
	# prnt = someList.pop()
	# print(pr/nt)

# In order for while statements to run properly, programmers usually define
# before the while header, and at the end of the while loop.
# count = 0
# while count < 20:
# 	print(count)
# 	count += 1

# It is possilble to have a loop inside of a loop
#for i in range(5):
#	for j in range(5):
#		print(i, j)

#############################################################################
# In ASCII code system "a" corresponds to 97, "z" to 122. A built-in Python
# function ord() returns that code value when a string with lenght 1 is input
# - the inverse function is chr().

# Let's say "a" indicates 1, "b" 2, ..., "z" 26. All othere characters are of
# 0 value. How "big" is the following sentence - technically speaking, string.

sent = "ars longa, vita brevis"
ls = []
count = 97
bigness = 0

while len(ls) < 26:
    ls.append(chr(count))
    count += 1

for i in sent:
    try:
        ls.index(i)
        i = ord(i) - 96
        bigness += i
    except ValueError:
        pass
print(bigness)

# sent = "ars longa, vita brevis"
# p sent.split('').map { |e| e.ord > 122 || e.ord <97 ? 0 : e.ord - 96  }.sum


sent = "ars longa, vita brevis"
bigness = 0

for i in sent:
    if i == " " or i == ",":
        pass
    else:
        i = ord(i) - 96
        bigness += i
print(bigness)
