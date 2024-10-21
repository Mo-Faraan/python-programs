""" Python code that removes duplicate elements from an array and returns the length of the remaining array without using sets or any built-in libraries like set(): """
def remove_duplicates(arr):
    if len(arr) == 0:
        return 0
    
    # Sort the array first
    arr.sort()
    
    # Initialize a pointer for the next unique element
    unique_index = 0
    
    # Iterate through the array
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[i]
    
    # The number of unique elements is the index of the last unique element + 1
    return unique_index + 1

# Example usage
arr = [1, 2, 2, 3, 4, 4, 5, 6, 6]
new_length = remove_duplicates(arr)
print(f"The length of the array after removing duplicates is: {new_length}")


