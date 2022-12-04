from readdb import readdatabase  # my own lybrary. 
from readcsv import readcsv      # my own lybrary
# Yes, I am probably reinvented the wheel, 
# I should have used libraries made by professional programmers.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


csvList1 = readcsv()      # made list datastructure (linked list)
dbList1 = readdatabase()  # made list datastructure (linked list)

CSVseries = pd.Series(csvList1)  # made a series from CSVlist using pandas library
DBseries = pd.Series(dbList1) # made a series from DBlist using pandas library
# series is pandas library datastructure. 
# We can print this seies using print(CSVseries) print(DBseries)

print('Data from csv file:')
print(csvList1)

print('Data from database file')
print(dbList1)

# Now we make bar diagram using matplotlib library
CSVindexes = CSVseries.index   # separated indexes from CSVseries
SCVvalues = CSVseries.values   # separated values from CSVseries
# print('Type of csv indexes array', type(CSVindexes))
Xvalues = np.array(CSVindexes)  # created numpy array from indexes 
Yvalues = np.array(SCVvalues)  # created numpy array from values
# values will be displayed on verical axis
plt.bar(Xvalues, Yvalues, color = 'red')  # made bar diagram using matplotlib library
plt.show()  # showed the bar diagram

# print(csvList1)
# print(dbList1) 

# Now we make bar diagram using matplotlib library
DBindexes = DBseries.index   # separated indexes from CSVseries
DBvalues = DBseries.values   # separated values from CSVseries
# print('Type of csv indexes array', type(CSVindexes))
Xvalues = np.array(DBindexes)  # created numpy array from indexes 
Yvalues = np.array(DBvalues)  # created numpy array from values
# values will be displayed on verical axis
plt.bar(Xvalues, Yvalues, color = 'green')  # made bar diagram using matplotlib library
plt.show()  # showed the bar diagram

# We will show descriptive statistics of CSVseries
# Now we make dataframe from CSVseries.  
# dataframe is pandas library datastructure
dfCSV = pd.DataFrame(CSVseries, columns=['Data'])
print('Dataframe from CSV file')
print(dfCSV)
print('Dataframe has descriptive statistics:')
print(dfCSV.describe())

# We will show descriptive statistics of DBseries
# Now we make dataframe from DBseries
# Now we make dataframe.  # dataframe is pandas library datastructure
dfDB = pd.DataFrame(DBseries, columns=['Temperature'])
print('Dataframe from DATBASE file')
print(dfDB)
print('Dataframe has descriptive statistics:')
print(dfDB.describe())




