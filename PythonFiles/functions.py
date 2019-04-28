##############################
#Functions
##############################


"""
There are two types of functions, built-in and custom.
Built-in functions have already been implemented and are ready to use by users.
print, is an example of a built-in function.
In this part of the course I am going to talk about custom functions.
Custom functions, which is an algorith built by us. 
You can write the function once, and use it as many times as you want it by just calling it.
"""

def potato_cost(quantity, price):
    cost=quantity*price
    return(cost)

#call the function
potato_cost(2,4)



def potato_cost(quantity, price, type_P):
    cost=quantity*price
    type_answer="The type is:"+" "+ type_P
    return(cost, type_answer)

#call the function
print (potato_cost(2,4,"red"))



def authenticate(password):
    if password=="Budapest":
        print ("Welcome")
    else:
        print ("re-insert Passowrd")

print(authenticate("Budapest"))
