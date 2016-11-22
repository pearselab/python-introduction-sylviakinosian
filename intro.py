#1. Write a loop that prints out the numbers 20 to 10

x = range(20, 10, -1)

for i in range(0,11):
    print(x[i])

#2. Write a list comprehension that returns the numbers from 20 to 10

listy = [x[i] for i in range(0,11)]

#3. Write a loop that prints out only even numbers from 20 to 10

for i in range(0,11):
    if x[i] % 2 == 0:
        print(x[i])

#4. Write a list comprehension that return only even number from 20 to 10

listEven = [x[i] for i in range(0,11) if x[i] % 2 == 0]

#5. Write a function that determines if a number is a prime number

#just trying to be clever
#def prime(n):
 #   x = range(n-1,1,-1)
  #  if n == 1:
   #     print "One isn't a prime number, dude"
    #for i in x:
     #   if x % i == 0:
      #      print 'not a prime number, brah'
    #else:
     #   print 'dood dis a prime number'

def prime(n):
  #  for i in range(n-1,1,-1):
    if n == 1:
        print "One isn't a prime number, dude"
    elif n % (n-1) == 0:
        print "DIS NOT PRIME"

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

