""" Give me the code, Python code, to merge two given sorted arrays so that the merged array is also sorted. """
def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i, j = 0, 0

    # Traverse both arrays and merge them into one
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # Append the remaining elements from arr1, if any
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    # Append the remaining elements from arr2, if any
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array

# Example usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merged = merge_sorted_arrays(arr1, arr2)
print(merged)
