def fibonacci(n):
    prev = 0
    current = 1
    print(prev)  # First Fibonacci number
    for i in range(1, n):  # Loop starts from 1 because 0th Fibonacci is already printed
        print(current)  # Print the current Fibonacci number
        temp = current
        current = prev + current  # Calculate the next Fibonacci number
        prev = temp  # Update the previous number to the current one

fibonacci(10)  # Generate the first 10 Fibonacci numbers
