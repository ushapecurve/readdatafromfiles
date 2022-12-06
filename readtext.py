def readtextfile():
    myfile = open('inputdata.txt','r') 
    #We shall open the txt file for reading data
    
    # we create a list. List is dynamically allocated array.
    mylist =  []
    numlines =  0
    
    for line in myfile:  #we make a loop and read every line in our file
        #print(line)
        words = line.split(',')  #words is array of strings. 
                                 #we will make it by splitting our line.
        for oneWord in words:          # we itterate through an array
            if oneWord == '\n':   #If there is end of line, we continue
                continue
            else:
                mylist.append(float(oneWord))
                #Appending data at the end of the list do not require
                #much computing power. O(1) complexity.
        numlines += 1
    
    
    #print(numlines)  # this is the number of lines
    #print(mylist)    # This list will contain all numbers that we read
                     #from file
    myfile.close()

    return mylist
