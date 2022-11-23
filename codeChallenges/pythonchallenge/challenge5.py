# Palindrome Check

def palindrome_check(str):
    # Using predefined function to reverse string
    rev = ''.join(reversed(str))
    if str == rev:
        return (str + ": This is a Palindrome")

    else:
        return (str + ": This is not a Palindrome")



#palindrome_check("madam")
#palindrome_check("Badam")
#palindrome_check("level")
#palindrome_check("Travel")

