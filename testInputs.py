#Determine if a float
# test = input('Input a number')
# user_input = int(test)
# float_input = user_input/2
# print('Your value is', float_input)

#Determind the temp
# test = float(input('input a temperature in C:'))
# if(test >= -278.15):
#     c = test - 278
#     print('The temperature is', c)

#Dtermine if Even/Odd
# input_number = int(input('input a number:'))
# if input_number % 2 == 0:
#     print("That's an even number ")
# else :
#     print ("That's an odd number")

#Determine if Prime
# n= int (input("Enter a number: "))
# is_prime = True
# for k in range (2,n):
#         if n % k == 0:
#             is_prime = False
# print('is_prime', is_prime)

#Define functions
# def greet(name):
#     print(f'Hello {name}, how are ya today?')
#
# user_name= str( input("What's your lovely name? "))
# greet(user_name)
# print("That's all for now")

#avg numbers
def avg(a,b):
    avg = (a+b) / 2
    return avg
x= int(input("ENTER THE FIRST NUMBER:: "))
y= int(input("ENTER THE SECOND NUMBER:: "))

avg= avg(x,y)
print(f'Your avg is:: {avg}')


