'''
Created on 08/apr/2015

@author: riccardo
'''

def create_file ():

    print "creating new file"
    print "Insert name and chapter number"
    name = raw_input("Name: ")
    chapter = raw_input("Chapter: ")
    
    fout = open(name + " - " + chapter, "w")
    
    print "Created text file with name %s" % name + " - " + chapter

    return fout

def translation ():
    page_count = 0
    b_count = 0
    sfx_count = 0
    line = ""
    result = " d"
    
    while line != "\q":
        line = raw_input("> ")
        if line.__eq__("\n"):
            pass
        if line == "\\n":
            print "qualcosa"
            page_count+=1
            print page_count
            b_count=0
            v = "PAGINA %d" % page_count
            result = result + v
            print "PAGINA %d" % page_count
        elif line == "\o":
            variation = raw_input("Insert variation: ")
            result.append (variation + " : ")
            variation = raw_input("Insert content: ")
            result.append (variation)
            
    print "Completed."
    print result
    

def main ():
    fout = create_file()
    print "Start translating"
    translation()
    
    fout.close()

if __name__ == '__main__':
    main()