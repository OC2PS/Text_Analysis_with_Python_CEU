
from collections import Counter

#create a function that has a string as input and returns as output  a list of the words in the string, without numbers and punctuations

def remove_junk_in_vec(text):
    junk_free="" 
    punc=[",", ".", "/;","'", "?", "&", "!", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(len(text)):
        #remove punctuation
        if text[i] not in punc:
            word=text[i].lower()
            junk_free=junk_free+word
    vec=junk_free.split()               
    return vec

file_read=open("Input/Barcelona.txt", 'r', encoding="utf-8") 
#read, readlines

content = file_read.readlines()
content=" ".join(content)

vec_of_words=[]
for sent in content.split():
    vec_of_words.extend(remove_junk_in_vec(sent))
    

file_write_barca=open("Outputs/Barcelona_counter_freq.txt", 'w') 
#write the first line with the name of the variables
file_write_barca.write("word" + ';' + "count" +  '\n')
#write each line
for key, value in Counter(vec_of_words).items(): 
    file_write_barca.write(key + ';' + str(value) +  '\n')
    
#provide an alternative way to write the dictionary to a .csv

file_write_barca.close()
