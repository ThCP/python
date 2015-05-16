'''
Implement a "print_words filename" program that, given a text file read from command line,
counts how often each word appears in the text and prints the results in the form

word1 count1
word2 count2

Created on 19/mar/2015

@author: riccardo
'''

#from sys import argv

#script, file_name = argv

txt = open("alice.txt")

# read = txt.read() I don't use this solution because it returns the reading of the whole file
# Instead, I use the following
read = txt.readline() # This statement returns only a line of the file, but stores in read only 1 char as string
read2 = txt.readlines() # This loops over the whole file and then returns the result in a list

'''
def cleanUp(newL):
    for i in newL:
        i.rstrip(',,.-:;!?')
        i.rstrip()
        i.lstrip('`')
        print i
    return newL
'''

words = {
         
         }        
for i in read2:
    new = i.rstrip()
    new = new.replace ("--", " ")
    newL = new.split(" ")
    newL = new.split(" ")
#    newL = cleanUp (newL)
    for j in newL:
        j = j.rstrip (",!.;:\'-?\")")
        j = j.lstrip ("(`-")
        if j in words:
            words[j] += 1
        else:
            words[j] = 1

for i in words:
    print "%s %d" % (i, words[i])
