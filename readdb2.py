import pyodbc
# server='DESKTOP-CSABO2K'
# database='tempandhummidity'
# username='sa'
# password='215pmMIXED'
# We will make trusted connection to named instance
dbConnection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=DESKTOP-CSABO2K;DATABASE=tempandhummidity;ENCRYPT=no;UID=sa;PWD=215pmMIXED;')
                              
           
cursor = dbConnection.cursor()

cursor.execute('SELECT [RecordID], [TimeStamp], [Temperature], [Hummidity] FROM [tempandhummidity].[dbo].[temperature] ')

for i in cursor:
    print(i)
    
    


