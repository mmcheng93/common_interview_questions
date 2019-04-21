def linear_search(data, x): 
    """Perform a linear search through a list (data) for a value called (x) and return the indices of the value."""
    indices = []
    for i in range (0, len(data)): 
        if (data[i] == x): 
            indices.append(i);
    return indices
    
if __name__ == "__main__":
    
    data = [] # A list of values to be searched
    x = 0  # A value you are looking for
    result = linear_search(data, x)
    if len(result) == 0: # If the value you are looking for is not in the list
        print(str(x) + " is not in the list.")
    else:
        indices = str(result).replace("[", "")
        indices = indices.replace("]", "")
        print(str(x) + " is present at the following indices " + indices)