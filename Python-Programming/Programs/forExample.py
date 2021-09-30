'''
FizzBuzz
Write a program that prints the numbers from 1 to 100. But for
multiplies of three print 'Fuzz' instead of the number and for
the multiplies of five print 'Buzz'. For numbers which are
multiples of both three and five print 'FizzBuzz'.
'''
for i in range(1, 20):
    s = str(i)
    if i%3 == 0 or i%5 == 0:
        s = ''
        if i%3 == 0:
            s = s + 'Fizz'
        if i%5 == 0:
            s += 'Buzz'
    print(s)
    