import re

def palindrome1(a_string):
# ^^^^   This is a O(n) - linear solution.  ^^^^
    # Increasing the length of the string would increase the processing time in a 'linear' fashion.
    # A longer string would take even longer so it isn't constant. 
    a_string = ''.join(filter(str.isalnum, a_string)).lower()

    # Slicing the string to reverse it requires the computer to iterate through each element in the string. 
    # This makes me think this also a O(n) -linear solution. 
    return a_string == a_string[::-1]

#************************************************************************************************

def palindrome2(a_string):
# ^^^^   This is a O(n) - linear solution.  ^^^^
    a_string = ''.join(filter(str.isalnum, a_string)).lower()

    # Assigning new variables takes up memory space but processing time is O(1)constant
    begin = 0
    end = len(a_string) -1

    # Using a two pointer approach makes this While loop a O(log n) - logarithmic command.
    # Rather than iterating once per element, we're iterating half that amount per element. 
    while begin <= end:
        # This if statement is O(1) - Constant. This wouldn't take longer with a longer string. 
        # Checking to see if the beginning of the string is equal to the end would take the same amount of time with a long string.
        if a_string[begin] != a_string[end]:
            return False    
        begin += 1
        end -= 1
    return True

# Even though this has some efficient lines of code using the two pointer approach, 
# this solution is probably O(n) - linear solution. The function is only as efficient as its slowest component.
# In this case (I belive) the slowest component is the filter function that looks for alphanumeric characters and removes whitespace.

#************************************************************************************************

def palindrome3(a_string):
    return re.sub(r'\W+', '', a_string).lower().replace(' ', '') == re.sub(r'\W+', '', a_string).lower().replace(' ', '')[::-1]
# ^^^^   This is a O(n) - linear solution.  ^^^^

# This function has to check every single element of the string. If the string were 'n' longer
# then the function would take 'n' longer. It would take proportionally long compared to the increase in length of the character.
