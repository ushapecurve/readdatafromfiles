from readdb import readdatabase  # my own module. 
from readtext import readtextfile      # my own module
# Yes, I am probably reinvented the wheel, 
# I should have used libraries made by professional programmers  
# like pandas.read_csv() pandas.read_sql().
# I will use pandas.read_CSV() in the neext phase of my project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2


txtList1 = readtextfile()      # made list datastructure (linked list)
dbList1 = readdatabase()  # made list datastructure (linked list)

txtPsandasSeries = pd.Series(txtList1)  # made a series object from TXTlist using pandas library
dbPandasSeries = pd.Series(dbList1) # made a series object from DBlist using pandas library
# series is pandas library datastructure. 
# We can print this seies using print(CSVseries) print(dbPandasSeries)

print('Data from text file:')
print(txtList1)
#print('Pandas series datastructure made from TXT file')
#print(txtPsandasSeries)  # series is just one dimentional array that can hold data of any type.

print('Data from database file')
print(dbList1)
#print('Pandas series datastructure made from TXT file')
#print(dbPandasSeries)  # series is just one dimentional array that can hold data of any type.

# Now we make bar diagram using matplotlib library
txtIndexes = txtPsandasSeries.index   # separated indexes from CSVseries
txtValues = txtPsandasSeries.values   # separated values from CSVseries
# print('Type of csv indexes array', type(CSVindexes))
xValues = np.array(txtIndexes)  # created numpy array from indexes 
yValues = np.array(txtValues)  # created numpy array from values
# values will be displayed on verical axis
plt1.bar(xValues, yValues, color = 'red')  # made bar diagram using matplotlib library
plt1.title('Temperatures read from TXT file')
plt1.ylabel('Temperatures, F')
plt1.xlabel('Number of measurement')
plt1.savefig('txtFileChart.png', dpi=600)
plt1.show()  # showed the bar diagram


# print(csvList1)
# print(dbList1) 

# Now we make bar diagram using matplotlib library
dbIndexes = dbPandasSeries.index   # separated indexes from CSVseries
dbValues = dbPandasSeries.values   # separated values from CSVseries
# print('Type of csv indexes array', type(CSVindexes))
xValues = np.array(dbIndexes)  # created numpy array from indexes 
yValues = np.array(dbValues)  # created numpy array from values
# values will be displayed on verical axis
plt2.bar(xValues, yValues, color = 'green')  # made bar diagram using matplotlib library
plt2.title('Temperatures read from Database file')
plt2.ylabel('Temperatures, F')
plt2.xlabel('Number of measurement')
plt2.savefig('dbFileChart.png', dpi=600)
plt2.show()  # showed the bar diagram

# We will show descriptive statistics of CSVseries
# Now we make dataframe from CSVseries.  
# dataframe is pandas library datastructure
dfTXT = pd.DataFrame(txtPsandasSeries, columns=['Data'])
#print('Dataframe from TXT file')
#print(dfTXT)
print('Dataframe from TXT file')
print('has descriptive statistics:')
print(dfTXT.describe())

# We will show descriptive statistics of dbPandasSeries
# Now we make dataframe from dbPandasSeries
# Now we make dataframe.  # dataframe is pandas library datastructure
dfDB = pd.DataFrame(dbPandasSeries, columns=['Temperature'])
#print('Dataframe from DATBASE file')
#print(dfDB)
print('Dataframe from DATBASE file')
print('has descriptive statistics:')
print(dfDB.describe())




