def anagram(s1, s2): 
    """Checks if two strings are anagrams or not."""
    # The alphabetically sorted strings are checked to see if they are the same as one another
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

if __name__ == "__main__":

    s1 = "silent" # First string
    s2 = "listen" # Second string
    anagram(s1, s2) # Run the strings through the checker