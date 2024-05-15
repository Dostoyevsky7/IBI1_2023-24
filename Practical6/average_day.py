#record and print out the average time of all the activities of a university student in a day
import matplotlib.pyplot as plt #import matplotlib to draw a graph
t_other = 24-8-6-3.5-2-1 #calculate the 'other' activity time
dict_time = {'Sleeping':8, 'Classes':6, 'Studying':3.5, 'TV':2, 'Music':1, 'Other':t_other}
#create a dictionary recording each activities and corresponding time
print(dict_time) #print out dictionary
choice = input("Choose one activity: ") #the user can choose an acitivity!
a_time = dict_time[choice] #know the time of the activity selected from the dictionary
print(a_time) #print out the time of the chosen activity

#this code got help from the course instructor Robert Young in IBI practical6 to draw a pie chart
label = ['Sleeping', 'Classes', 'Studying', 'TV', 'Music', 'Other'] #set the labels for all the acitivities in the chart
time = [8,6,3.5,2,1,t_other] 
plt.figure()
plt.pie(time, labels=label, startangle=90) #draw a pie chart, the starting angle is 90 degree
plt.title("the average day of a university student") #add a title to this figure
plt.show()
plt.clf() #clear relevant data