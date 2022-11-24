import pyodbc
server='DESKTOP-CSABO2K'
database='tempandhummidity'
username='sa'
password='215pmMIXED'
# We will make trusted connection to named instance
connection = pyodbc.connect('DRIVER={ODBC Driver18 for SQL Server};SERVER='+server+';DATABASE='+database+'ENCRYPT=yes;UID='+username+'PWD='+password);
