# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:41:28 2019

@author: Anna
"""

def remove_quiz(text):
        text2=str(text)
        junk_free="" 
        punc=[",", ".", "/;","'", "?", "&", "!", "-", "[", "]", "(", ")", ":", ";"]
        for i in text2:
            if i not in punc:
                word=i.lower()
                junk_free=junk_free+word
        return junk_free
    

e="iwilldelete.every,thing:(000)"
print(remove_quiz(e))

##i will recode the type as string in the line9, the numbers will be in my code, in case of you want to delete it put it to the punc function