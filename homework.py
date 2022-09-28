# [ log(n), n, n**2, n**3 ]

# A phrase is a  if, after converting all uppercase letters 
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include 
# letters and numbers.
# Given a string s, return true or false.
 
# s = "A man, a plan, a canal: Panama"
# true
# "amanaplanacanalpanama" is a palindrome.

# s = "race a car"
# false
# "raceacar" is not a palindrome.

# s = " "
# true
# s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

'''
Outline:

make a function with a string as a parameter
remove any unwanted characters
check if the string is spelled the same backwards
if it is, return True
if it isn't return False

'''
def palindrome(astring):
    new_string = ""
    for item in astring:
        if item.isalnum():
            new_string += item.lower()
    if new_string[::-1] == new_string:
        return True
    else:
        return False

print(palindrome("A man, a plan, a canal: Panama"))

# The time complexity is "n" time