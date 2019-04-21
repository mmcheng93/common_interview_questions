def fibonacci(n):
    """Function for nth Fibonacci number."""
    a = 0
    b = 1
    if n == 1: # First number in the Fibonacci Sequence is 0
        return a
    elif n == 2: # Second number in the Fibonacci Sequence is 1
        return b
    else:
        for i in range(2,n): #Fibonacci Sequence is F(n) = F(n-1) + F(n-2)
            c = a + b
            a = b
            b = c
        return b
    
if __name__ == "__main__":
    
    flag = 1
    while flag != 0:
        n = int(input("Enter the nth number in the Fibonacci Sequence you want or a number <= 0 to exit. "))
        if n > 0:
	        print(fibonacci(n))
        else:
            flag = 0