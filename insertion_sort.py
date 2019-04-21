def insertion_sort(data, x): 
    """Insert a new element into a list in the correct order."""
    data.sort() # Sort the list in ascending order
    # Traverse through list
    for i in range(0, len(data)): 
        if x > data[i] and x < data[i+1]:
            new_list = data[:i+1] + [x] + data[i+1:]
    return new_list

if __name__ == "__main__":

    data = [4,2,7,12] # A list of values to be searched
    x = 3  # A value you are looking for
    result = insertion_sort(data, x)
    print(result)