


##############################
#Sequences, collections and iterations
##############################

#(SEQUENCES) lists and tuples

"""
#Python has a great built-in list type named "list". 
List literals are written within square brackets [ ]. 
Lists work similarly to strings -- use the len() function and square brackets [ ] 
to access data, with the first element at index 0

*access the elements of the list
*append and extend elements in list

In case you don't want your list to be modified, in this case we use tupples.
To declare a list we use square brackets, instead for tuples we use round brackets

Tuples are rarely used, but they are indeed used.
"""



MyList=["a", "B", "b", "c", "a"]
#append and extend the list

MyList.append("f")
MyList.extend("g")
#["j", "i", "l"]

#get the first element on a list (index)

MyList[0]

#get the last element on a list
#first we need to know the length of the list
len(MyList)
MyList[4]
MyList[len(MyList)-1]
#or alternatively
MyList[-1]

#convert list to tuple 
FromListToTuple=tuple(MyList)

#we can convert the list using the set function
MySet=set(MyList)
#The duplicates have now been removed

#set is also generated
NewSet={2013,2015,2016}


#you can convert a set into a list using the list function
#A set is an unordered collection with no duplicate elements. 
MyNewList=list(MySet)



for item in [1,5,9,6,9]:
	print(item)

new_list=[1,5,9,6,9]
#we can also iterate in the following way
[item for item in new_list]
[item for item in [1,5,9,6,9]]

#square all elements in a list

[i**2 for i in new_list]



#Dictionaries are composed of key and values

"""
Each key is separated from its value by a colon (:), the items are separated by 
commas, and the whole thing is enclosed in curly braces. 
An empty dictionary without any items is written with just two curly braces, 
like this: {}.

Keys are unique within a dictionary while values may not be. 
The values of a dictionary can be of any type, 
but the keys must be of an immutable data type such as strings, numbers, or tuples.
"""

#https://www.tutorialspoint.com/python/python_dictionary.htm
tel = {'jack': 4098, 'rose': 4139}
tel['guido'] = 4127
tel

#acess a key
tel['jack']

#delete a key
del tel['kate']
#list keys
list(tel.keys())
#sort keys
sorted(tel.keys())
sorted(tel.values())
#fast check if a key is in the dictionary
'guido' in tel

'ari' in tel

