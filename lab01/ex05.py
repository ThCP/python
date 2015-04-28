# exercise 05
# given a list of strings, return the count of the number of Strings
# where the string length is 2 or more and the first and last chars 
# of the string are the same

input_list = ['aba', 'xyz', 'aa', 'x', 'bbb']

count = 0

print "The input is %r " % input_list

for element in input_list:
    if len(element) >= 2:
        if element[0] == element[len(element)-1]:
            count+=1;
        
print "The result is %d" % count

