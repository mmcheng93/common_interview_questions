def palindrome(s):
    """Reverses a string and checks to see if the reversed string is the same as the original string."""
    rev = s[::-1] # Reverse the string [start,stop,step]
    # Checking if both string are equal or not 
    if (s == rev): 
        print(s + " IS a palindrome")
    else:
        print(s + " is NOT a palindrome")

if __name__ == "__main__":

    s = "tattarrattat" # String
    palindrome(s) # Run the string through the checker