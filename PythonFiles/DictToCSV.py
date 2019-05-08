#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
os.chdir("")


#import string
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt


file_read=open("Input/Barcelona.txt",'r',encoding="utf-8") 
import re
words_counts=[]
for line in file_read:
    #non alpha numeric characters in a string
    s = re.sub('[^0-9a-zA-Z]+', ' ', line)
    print (s)
    #remove all but alphanumeric from string
    print(re.sub(r'\W+', ' ', s))
    new_string=re.sub('[^a-zA-Z]+', ' ', s)
    #convert the string to lower case letters
    new_string=new_string.lower()
    #split the string and create a vector of all strings
    vect=new_string.split()
    words_counts.extend(vect)
    
    
dict_counts=Counter(words_counts)
labels, values = zip(*dict_counts.items())
    
    
# sort your values in descending order
indSort = np.argsort(values)[::-1]

# rearrange your data and show top 5 words
labels = np.array(labels)[indSort][0:5]
values = np.array(values)[indSort][0:5]

indexes = np.arange(len(labels))

bar_width = 0.03

plt.bar(indexes, values)

# add labels
plt.xticks(indexes + bar_width, labels)
plt.show()


#access the first two keys of the dictionary
dict_counts["the"]
dict_counts["of"]

#write it in a file

fi=open('Outputs/Barcelona_counter_freq.txt', 'w') 
fi.write('word' +";" +"frequency\n")
for key, value in Counter(dict_counts).items():
    print (key, value)
    fi.write(key + ';' + str(value) +  '\n')
fi.close()
    

    
#the last bit you could also do it in the following way:
"""
import csv

with open('Outputs/Barcelona_counter.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(['word','frequency'])
    for key, value in dict_counts.items():
       writer.writerow([key, value])
"""
