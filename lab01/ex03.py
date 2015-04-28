# exercise 3
# Given a string s, return a string made of
# the first two and the last two
# chars of the original string.

def newF (s):
    if len (s) <= 2:
        return ""
    else:
        return s[0:2]+s[len(s)-2:len(s)]


s = raw_input("Insert the string: ")

result = newF(s)

print result        