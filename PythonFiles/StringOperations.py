

#In python strings are concatenated using +
str1 = "Budapest"
str2 = "is a beautiful city"
full_string=str1+" "+ str2



#another way to concatenate is via the join method

full_string2= "".join([str1, " ", str2])

full_string3= " ".join([str1,str2])

#check if they all give the same result
full_string==full_string2==full_string3

#string split 
full_string.split()
full_string.lower()
full_string.upper()

string_with_spaces="  Budapest is  an   amazing city"
full_string.strip("B")
string_strip=string_with_spaces.strip()

#try also rstrip and lstrip


"""
#returns a boolean
isalpha() letters only
isalnum() letters and numbers only
isdecimal() numbers only
isspace() spaces only
istitle() titles only

startswith()
endswith()
"""



#this can be better done with regular expressions
#import the regular expression library
"""
check https://docs.python.org/2/library/re.html
A regular expression (or RE) specifies a set of strings that matches it; 
the functions in this module let you check if a particular string matches a 
given regular expression (or if a given regular expression matches a particular
 string, which comes down to the same thing).
"""
import re
re.sub(' +',' ',string_with_spaces)


 #we can also operate in lists of string in a different way

#let's create a string with punctuation

poem="Some say the world will end in fire, Some say in ice."

#we want to remove punctuation and numbers

#one way to go is the following

punc=[",", ".", "/;","'", "?", "&", "!", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbol_free="" 

for char in poem:
    if char not in punc:
        symbol_free=symbol_free+char

#now convert all letters in lower case 
symbol_free=symbol_free.lower()

#convert it to vector
vec_symbol_free=symbol_free.split()



#let's create a function that takes every string and converts it into a clean string

def remove_junk(text):
    junck_free="" 
    punc=[",", ".", "/;","'", "?", "&", "!", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(len(text)):
        if text[i] not in punc:
            word=text[i].lower()
            junck_free=junck_free+word
    return junck_free

print(remove_junk(poem))

print(remove_junk("Let's see how176 we could deal with puntuation and numbers 23."))


def remove_junk_in_vec(text):
    junck_free="" 
    punc=[",", ".", "/;","'", "?", "&", "!", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(len(text)):
        if text[i] not in punc:
            word=text[i].lower()
            junck_free=junck_free+word
    vec=junck_free.split()               
    return vec
    
print(remove_junk_in_vec(poem))
text2="Let's see how176 we could deal with puntuation and numbers 23."
print(remove_junk_in_vec(text2))
  

#you could also do a combination of functions
def remove_junk_in_vec2(text):
    vectorized=remove_junk(text).split() 
    return vectorized
    

print("version2", remove_junk_in_vec(poem))
text2="Let's see how176 we could deal with puntuation and numbers 23."
print("version2", remove_junk_in_vec(text2))


#Another way to rempve punctuation is to use regular expressions 
new_string=re.sub(r'([^\s\w]|_)+', '', poem)
#you could also apply the fuction lower to the string

new_string=re.sub(r'([^\s\w]|_)+', '', poem).lower()

#now check again if the strings are similar
symbol_free==new_string
#We are done :-)

#another way to go is with the string library
import string

# Check characters to see if they are in punctuation
nopunc = [char for char in poem if char not in string.punctuation]

# Join the characters again to form the string.
nopunc = ''.join(nopunc).lower()

symbol_free==new_string==nopunc

#for more on regular expressions check https://www.debuggex.com/cheatsheet/regex/python
#to test your regular expressions check http://pythex.org/
#https://regexone.com/references/python

