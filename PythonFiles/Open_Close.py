
#import the libraries
import os
from collections import Counter
#here you can change the directory that is on your on computer
os.chdir("")

f=open("first_file.txt",'w') 

#write the 
id_n=["B3","B4","B5","B6"]


for item in id_n:
    f.write(item+"\n")
f.close()

#create a function that has a string as input and returns as output  a list of the words in the string, without numbers and punctuations

def remove_junk_in_vec(text):
    junk_free="" 
    punc=[",", ".", "/;","'", "?", "&", "!", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(len(text)):
        #remove punctuation
        if text[i] not in punc:
            word=text[i].lower()
            junck_free=junk_free+word
    vec=junck_free.split()               
    return vec

file_read=open("Input/Barcelona.txt", 'r', encoding="utf-8") 

vec_of_words=[]
for line in file_read:
    #iterate only through lines that are non empty
    if len(line)>0:
        vec_of_words.extend(remove_junk_in_vec(line))
    

file_write_barca=open("Outputs/Barcelona_counter_freq.txt", 'w') 
#write the first line with the name of the variables
file_write_barca.write("word" + ';' + "count" +  '\n')
#write each line
for key, value in Counter(vec_of_words).items(): 
    file_write_barca.write(key + ';' + str(value) +  '\n')

file_write_barca.close()

    
    
    



