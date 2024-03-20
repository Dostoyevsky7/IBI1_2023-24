t_other = 24-8-6-3.5-2-1 #calculate the 'other' activity time
dict_time = {'Sleeping':8, 'Classes':6, 'Studying':3.5, 'TV':2, 'Music':1, 'Other':t_other} #create a dictionary
print(dict_time) #print out dictionary
print(dict_time['Sleeping']) #the part 'Sleeping' can change depends on the user
#print the amount of time of a certain activity on the list
import numpy as np
import matplotlib.pyplot as plt
label = ['Sleeping', 'Classes', 'Studying', 'TV', 'Music', 'Other']
time = [8,6,3.5,2,1,t_other]
plt.figure()
plt.pie(time, labels=label, startangle=90) #draw a pie chart
plt.title("the average day of a university student") #add a title to this figure
plt.show()
plt.clf()
choice = input("choose one activity: ") #the user can choose an acitivity!
a_time = dict_time[choice] #the part 'Sleeping' can change depends on the user
print(a_time) #print the amount of time of a certain activity on the list