
"""
Variables in Python can be considered as containers. They contain everything.
By assigning different data types to variables, you can store integers, decimals or characters in these variables.
"""

FlowerPrice=3.5 # a float
FlowerType="Tuilpan" #a string

#In Python you can overwrite a variable
FlowerPrice=5 # an integer

print (type(FlowerPrice))
print (type(FlowerType))

#Also convert an integer to string 

FlowerPrice=str(FlowerPrice)

#And convert it back to integer (or float)
FlowerPrice=int(str(FlowerPrice)) or #FlowerPrice=float(str(FlowerPrice))
