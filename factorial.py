number = int(input("Enter the number to calculate the factorial\n"))
fact = 1
for i in range(1, number + 1):
    fact = fact * i

print("Factorial of the given number is", fact)
