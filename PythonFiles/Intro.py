
"""
Variables in Python can be considered as containers. They contain everything.
By assigning different data types to variables, you can store integers, decimals or characters in these variables.
"""

FlowerPrice=3.5
#In Python you can overwrite a variable
FlowerPrice=5

FlowerType="Tuilpan"

print (type(FlowerPrice))
print (type(FlowerType))

#Also convert it to string 

FlowerPrice=str(FlowerPrice)

#And convert it back to integer (or float)
FlowerPrice=int(str(FlowerPrice))

#FlowerPrice=float(str(FlowerPrice))

print("Hello World!!!")
