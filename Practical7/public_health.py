import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv") #use pandas to read a csv document
print(dalys_data.head(7)) #print the first 5 rows in the file
dalys_data.info() #return the data types and othe rinformation
print(dalys_data.describe()) #return mean, std, min&max, 25%, 50%, 75% of the data
#mean DALYs = 42372.219173, max = 693367.490000, min = 15045.110000

#use iloc to print out values
dalys_data.iloc[0,3] # iloc[row,column]: print the value on this location
dalys_data.iloc[1,0:3]
dalys_data.iloc[0:3,:] #':'means all
dalys_data.iloc[0:10:2,:] #'0:10:2'means 0,2,4,6,8 that is [0,10), difference=2
dalys_data.iloc[0:10:2,0:8] #if there are no 9 columns, return all the 4 columns
print(dalys_data.iloc[0:101:10,:]) 
print(dalys_data.iloc[0:3,[0,1,3]]) #row0,1,2 and column0,1,3
dalys_data.iloc[0:3,[True, False, True, True]] #shows the columns with value=True
#dalys_data.iloc[0:3,[True, False, True]] #when the Boolean is shorter than the data, error!
#dalys_data.iloc[0:3,[True, False, True,True, False]] #error too because there are 5 instead of 4!

#use loc to print out values
dalys_data.loc[2:4,'Year'] #loc is [2,4], 2&4 both included
#to print out all the data of "Afghanistan"
find_list = []
for i in range(6840):
    if dalys_data.iloc[i,0] == 'Afghanistan':
        find_list.append(True)
    else:
        find_list.append(False)
print(dalys_data.iloc[find_list,:])

#pick out data from china
china_list = []
for i in range(6840):
    if dalys_data.iloc[i,0] == 'China':
        china_list.append(True)
    else:
        china_list.append(False)
china_data = dalys_data.iloc[china_list,[0,2,3]]
average_china = np.mean(china_data.loc[:,'DALYs'])
print(average_china) #average = 30677.694333, smaller than DALYs of 2019
plt.figure()
plt.plot(china_data.Year, china_data.DALYs, 'r+') #r+ means red-colour "+" as the number dots
plt.xticks(china_data.Year, rotation=-90) #rotation=-90 means rotate 90 degrees anti-clockwise
plt.show()
plt.clf()

#solve the questions
#first store the data of China and UK respectively
#data of China has already stored in previous lines(line 36-42) in china_data
#store UK data
uk_list = []
for i in range(6840):
    if dalys_data.iloc[i,0] == 'United Kingdom':
        uk_list.append(True)
    else:
        uk_list.append(False)
uk_data = dalys_data.iloc[uk_list,[0,2,3]]
#draw a picture of both UK and China DALYs data
plt.figure()
plt.plot(china_data.Year, china_data.DALYs, 'r+', label='China') #r+ means red-colour "+" as the number dots
plt.plot(uk_data.Year, uk_data.DALYs, 'b+', label='UK')
plt.xticks(china_data.Year, rotation=-90) #rotation=-90 means rotate 90 degrees anti-clockwise
plt.xlabel("Years")
plt.ylabel("DALYs")
plt.legend()
plt.show()
plt.clf()