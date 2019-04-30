
#import the libraries
import os
#here you can change the directory that is on your on computer
os.chdir("")
f=open("Outputs/first_file.txt",'w') 

#write the 
id_n=["B3","B4","B5","B6"]


for item in id_n:
    f.write(item+"\n")
f.close()


    
    



