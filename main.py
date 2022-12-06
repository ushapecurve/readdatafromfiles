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


TxtList1 = readtextfile()      # made list datastructure (linked list)
DbList1 = readdatabase()  # made list datastructure (linked list)

TxtSeries = pd.Series(TxtList1)  # made a series from CSVlist using pandas library
DbSeries = pd.Series(DbList1) # made a series from DBlist using pandas library
# series is pandas library datastructure. 
# We can print this seies using print(CSVseries) print(DBseries)

print('Data from csv file:')
print(TxtList1)

print('Data from database file')
print(DbList1)

# Now we make bar diagram using matplotlib library
TxtIndexes = TxtSeries.index   # separated indexes from CSVseries
TxtValues = TxtSeries.values   # separated values from CSVseries
# print('Type of csv indexes array', type(CSVindexes))
Xvalues = np.array(TxtIndexes)  # created numpy array from indexes 
Yvalues = np.array(TxtValues)  # created numpy array from values
# values will be displayed on verical axis
plt1.bar(Xvalues, Yvalues, color = 'red')  # made bar diagram using matplotlib library
plt1.title('Temperatures read from TXT file')
plt1.ylabel('Temperatures')
plt1.xlabel('No of measurement')
plt1.show()  # showed the bar diagram

# print(csvList1)
# print(dbList1) 

# Now we make bar diagram using matplotlib library
DbIndexes = DbSeries.index   # separated indexes from CSVseries
DbValues = DbSeries.values   # separated values from CSVseries
# print('Type of csv indexes array', type(CSVindexes))
Xvalues = np.array(DbIndexes)  # created numpy array from indexes 
Yvalues = np.array(DbValues)  # created numpy array from values
# values will be displayed on verical axis
plt2.bar(Xvalues, Yvalues, color = 'green')  # made bar diagram using matplotlib library
plt2.title('Temperatures read from Database file')
plt2.ylabel('Temperatures')
plt2.xlabel('No of measurement')
plt2.show()  # showed the bar diagram

# We will show descriptive statistics of CSVseries
# Now we make dataframe from CSVseries.  
# dataframe is pandas library datastructure
DfTXT = pd.DataFrame(TxtSeries, columns=['Data'])
print('Dataframe from TXT file')
print(DfTXT)
print('Dataframe has descriptive statistics:')
print(DfTXT.describe())

# We will show descriptive statistics of DBseries
# Now we make dataframe from DBseries
# Now we make dataframe.  # dataframe is pandas library datastructure
dfDB = pd.DataFrame(DbSeries, columns=['Temperature'])
print('Dataframe from DATBASE file')
print(dfDB)
print('Dataframe has descriptive statistics:')
print(dfDB.describe())




