# exercise 4
# Given a list of string s, return a string in which all the occurrences
# of the first character have been  changed to '*', except the first char
# The string must be inserted by the user.

s = raw_input("Insert string: ")

first = s[0]

partial = s.replace(str(first), "*")

result = first + partial[1:len(partial)]

print "result = %s" % result

