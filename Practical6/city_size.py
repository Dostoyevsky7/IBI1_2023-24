import matplotlib.pyplot as plt #import matplotlib to draw a graph later
uk_cities = [0.56, 0.62, 0.04, 9.7]
uk_cities.sort() #sort the population number from samll to large
chn_cities = [0.58, 8.4, 29.9, 22.2]
chn_cities.sort()
print(uk_cities)
print(chn_cities)
#print out 2 lists in sorted order

#the bar chart of UK
#this code got help from the course instructor Robert Young in IBI practical6 to draw a bar chart
ind1 = ['Stirling', 'Edinburgh', 'Glasgow', 'London'] #the indexes are the names of the cities
width1 = 0.5 
plt.figure() #import a function in matplotlib
plt.bar(ind1, uk_cities, width1, color = 'cornflowerblue') # choose a blue color
plt.ylabel("population(millions)") # the label of the y axis is the population with the unit of million
plt.title("population of different cities in UK") #add a chart title
plt.xticks(ind1) # the lables of x axis is the list above listing city names
plt.show() #show the graph
plt.clf() #close the graph and relevant data

#the bar chart for China
#this code got help from the course instructor Robert Young in IBI practical6 to draw a bar chart
ind2 = ['Haining', 'Hangzhou', 'Beijing', 'Shanghai']
width2 = 0.4 #choose the width of each bar
color_option = ['brown', 'firebrick', 'indianred', 'lightcoral'] #every bar can have a different color
plt.figure() 
plt.bar(ind2, chn_cities, width2, color = color_option) #change the width to 0.3
plt.ylabel("population(millions)") # the lable of the y axis the population with the unit of million
plt.title("population of different cities in China") #add a chart title
plt.xticks(ind2) # the lables of x axis is the list above listing city names
plt.show() #show the graph
plt.clf() #clear data