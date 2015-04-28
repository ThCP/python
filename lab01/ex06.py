# exercise 6
# Given a list of strings, return a list with the strings in sorted
# order, but grouping  all the strings that begin with 'x' first.

Input = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
list_x =[]
list_else =[]


for i in Input:
    if i[0] == 'x':
        list_x.append(i)
    else:
        list_else.append(i)
    
print Input
print list_x
print list_else

#sorted_list = sorted(Input)
list_x.sort()
list_else.sort()

print "final list "
print  list_x + list_else