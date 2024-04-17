d=5 #the initial density is 5%
dayscount=1 #count the days that can be away from the lab
while d<=90:
    dayscount=dayscount+1
    d=d*2
t=str(dayscount) #str() transfer a number to a string
print("on day"+t+" the density grows over 90%!")
r=dayscount-1
h=str(r) 
print("you can have a holiday for "+h+" days at maximum!")
### attention the initial dayscount is 1 or 0!!!