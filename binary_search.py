def binary_search(data, x): 
    """Performs a iterative binary search that cursor the list each time when searching for an value until the list could not be halved any more."""
    last = len(data) - 1 # Index of last element in list currently be searched
    cursor = 0 # Index of the current value being treated as the element we are looking for
    
    while cursor <= last: 
  
        mid = cursor + (last - cursor)/2; 
          
        # Check if x is present at mid 
        if data[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif data[mid] < x: 
            cursor = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            last = mid - 1
      
    # If we can't halve the list anymore, then the element was not present 
    return -1
  
if __name__ == "__main__":

    data = [] # A list of values to be searched
    x = 0  # A value you are looking for
    result = linear_search(data, x)
    if result != -1: 
        print("Element is present at index " + str(result) + ".")
    else: 
        print("Element is not present in array!")