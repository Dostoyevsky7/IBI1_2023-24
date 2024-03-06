###3.1 simple math
a = 40
b = 36
c = 30
d = a-b
e = b-c
if d > e:
    print('yes')
else:
    print('no')
#how can the program feed back a boolean value directly?
#if there is no if loop, the running outcome is nothing
###d<e, so the running and strength traning regime has a greater effect

###3.2 booleans
X= True
Y= False
#if X=True, Y=True, then W=False;
#if X=True, Y=False, then W=True (vise versa)
if X and Y == True or X or Y == False:
    W= False
else:
    W= True
print(W)

X= True
Y= False
if X and Y == True:
    W=False
elif X or Y == False:
    W= False
else:
    W=True
print(W)

#A more brilliant way!:
X= True
Y= False
if X==Y:
    W=False
else:
    W=True
print(W)

##the true table of W:
##X=True, Y=True, W=False
##X=True, Y=False, W=True
##X=False, Y=True, W=True
##X=False, Y=False, W=False