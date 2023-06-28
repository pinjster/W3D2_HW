# You need to write a function, that returns the first non-repeated character in the given string.

# If all the characters are unique, return the first character of the string.
# If there is no unique character, return None.

# You can assume, that the input string has always non-zero length.

# Examples
# "test"   returns "e"
# "teeter" returns "r"
# "trend"  returns "t" (all the characters are unique)
# "aabbcc" returns None (all the characters are repeated)

#for loop
#new list 
#int for each char
#loop
#return first char that has a value of 1

def uniquechar(word):
    word = word.lower()
    for char in word:
        count = 0
        for item in word:
            if char == item:
                count += 1
        if count == 1:
            return char
    return None

print(uniquechar("aabbcc"))
