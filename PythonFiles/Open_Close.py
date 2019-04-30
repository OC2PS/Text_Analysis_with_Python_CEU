
#import the libraries
import os
#here you can change the directory that is on your on computer. Remind to use / instead of \. The first is compatible across platforms.
os.chdir("")
f=open("Outputs/first_file.txt",'w') 

#write the 
id_n=["B3","B4","B5","B6"]

for item in id_n:
    f.write(item+"\n")
f.close()


"""
f=open("Outputs/first_file.txt",'w') 

#write the 
id_n=["B3\n","B4\n","B5\n","B6\n"]

for item in id_n:
    f.write(item)
f.close()
"""
