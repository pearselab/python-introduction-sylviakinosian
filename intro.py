#1. Write a loop that prints out the numbers 20 to 10

x = range(10,21)
y = sorted(x, reverse=True)

for i in range(0,11):
    print(y[i])

#2. Write a list comprehension that returns the numbers from 20 to 10

listy = [y[i] for i in range(0,11)]

#3. Write a loop that prints out only even numbers from 20 to 10

for i in range(0,11):
    if y[i] % 2 == 0:
        print(y[i])

#4. Write a list comprehension that return only even number from 20 to 10

listEven = [y[i] for i in range(0,11) if y[i] % 2 == 0]

#5. Write a function that determines if a number is a prime number

def prime(x):
    if x == 1:
        print "One isn't a prime number, dude"
    for i in range(x,2);
        if i % 2


#6. Write a function that loads a text file, loops over the lines in it, and
# prints out the fifth character of the fifth line of that file

with open("name of file") as handle:
    for line in handle:
        do something

#7. Write a loop that prints out the numbers from 1 to 20, printing "

def factorial(x):
    if x == 1:
        return(x)
    return 

