uk_cities = [0.56, 0.62, 0.04, 9.7]
uk_cities.sort()
chn_cities = [0.58, 8.4, 29.9, 22.2]
chn_cities.sort()
print(uk_cities)
print(chn_cities)
#print out 2 lists
import numpy as np
import matplotlib.pyplot as plt
#import 2 librabries

#the bar chart of UK
ind1 = ['Stirling', 'Edinburgh', 'Glasgow', 'London'] #the indexes are the names of the cities
width1 = 0.5
plt.figure()
plt.bar(ind1, uk_cities, width1, color = 'cornflowerblue') # choose a blue color
plt.ylabel("population(millions)")
plt.title("population of different cities in UK") #add a chart title
plt.xticks(ind1)
plt.show()
plt.clf()

#the bar chart for China
ind2 = ['Haining', 'Hangzhou', 'Beijing', 'Shanghai']
width2 = 0.3
color_option = ['brown', 'firebrick', 'indianred', 'lightcoral'] #every bar can have a different color
plt.figure()
plt.bar(ind2, chn_cities, width2, color = color_option) #change the width to 0.3
plt.ylabel("population(millions)")
plt.title("population of different cities in China")
plt.xticks(ind2)
plt.show()
plt.clf() #remember to type clf