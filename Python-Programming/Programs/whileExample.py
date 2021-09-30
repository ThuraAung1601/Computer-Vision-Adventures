'''
Page - 24
Write a program that asks the user to input 10 integers, and then prints
the largest odd number that was entered. If no odd number was entered,
it should print a message to that effect.
'''
repeat = 10
large = 0

while repeat:# != 0:
    num = eval(input("Please enter 10 integers: "))
    
    if num%2 != 0 and num > large:
            large = num
    
    repeat -= 1
        
if large == 0:
    print("\nYou do not enter odd number.")
else:
    print("\nThe largest odd number is", large)
