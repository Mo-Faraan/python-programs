""" Give me a Python code to check whether a given string is palindrome or not after removing an element from any index in that string. """
def is_palindrome(s):
    return s == s[::-1]

def can_be_palindrome_by_removing_one_char(s):
    n = len(s)
    
    # Check if the string is already a palindrome
    if is_palindrome(s):
        return True
    
    # Try removing each character and check if the remaining string is a palindrome
    for i in range(n):
        modified_string = s[:i] + s[i+1:]
        if is_palindrome(modified_string):
            return True
    
    return False

# Example usage
string = input("Enter a string: ")
if can_be_palindrome_by_removing_one_char(string):
    print("Yes, it can be a palindrome by removing one character.")
else:
    print("No, it cannot be a palindrome even after removing one character.")
