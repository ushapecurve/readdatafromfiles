def readdatabase():
    import pyodbc
    # server='DESKTOP-CSABO2K'
    # database='tempandhummidity'
    # username='sa'
    # password='215pmMIXED'
    # We will make trusted connection to named instance
    dbConnection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=DESKTOP-CSABO2K;DATABASE=tempandhummidity;ENCRYPT=no;UID=sa;PWD=215pmMIXED;')
                                  
               
    cursor = dbConnection.cursor()
    
    cursor.execute('SELECT [RecordID], [TimeStamp], [Temperature], [Hummidity] FROM [tempandhummidity].[dbo].[temperature] ')
    # After execiting this statement, the cursor object contains
    #inside a list of tupples
    
    # we create a list. List is dynamically allocated array.
    mylist =  []
    
    for row in cursor:
        #print(row)  # we print each of these tupples
        #one at a time.
        
        #print(row[2]) # we print the second item of each tupple.
        #which is the numbers from Tempertature column from the 
        #DATABASE=tempandhummidity Table=[tempandhummidity].[dbo].[temperature]
        mylist.append(float(row[2]))
        
        
    #print(mylist)
    cursor.close()
    dbConnection.close()
    return mylist 
        


