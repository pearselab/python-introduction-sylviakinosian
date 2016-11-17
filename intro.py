#1 Write a loop that prints out the numbers 20 to 10

x = range(10,21)
y = sorted(x, reverse=True)

for i in range(0,11):
    z = y[i]
    print(z)

#2 Write a list comprehension that returns the numbers from 20 to 10

listy = [y[i] for i in range(0,11)]

#3 Write a loop that prints out only even numbers from 20 to 10

for i in range(0,11):
    if y[i] % 2 == 0:
        print(y[i])

#4 Write a list comprehension that return only even number from 20 to 10

listEven = [y[i] for i in range(0,11) if y[i] % 2 == 0]

# Write a function that determines in a number is a prime number


