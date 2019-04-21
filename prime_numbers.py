def prime_numbers(a, b):
    """This function returns all prime numbers in a list between a and b."""
    result = []
    for val in range(a, b + 1):
        if val > 1: 
            for n in range(2, val): 
                if (val % n) == 0: # If num is divisible by any number between 2 and val, it is not a prime number
                    break
            else:
                result.append(val) # If num is not divisible by any number between 2 and val, it is a prime number
    return result

if __name__ == "__main__":
    
    flag = 1
    while flag != 0:
        a = int(input("Enter the LOWER LIMIT of the range over which you want all the prime numbers from or 0 to exit. "))
        if a != 0:
            b = int(input("Enter the UPPER LIMIT of the range over which you want all the prime numbers from. "))
            print(prime_numbers(a, b))
        else:
            flag = 0