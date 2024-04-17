# use for loop: pre-set 5 times of calculations
a=4
print(a)###how to include a=4 i and print out in the loop?
for i in range (1,5):
    a=2*a+3 #assign a new value to a new a
    print(a)

# use while loop: make the final value is 109
a=4
print(a) #why cant involve the initial a into the loop?
while a<109: #attention this is < not <=!!! because if <=, 109 would satisfy the loop again
    a=2*a+3
    print(a)

#define a new function(something learnt in highschool lol)
def A(n): #define a new function called A(n)
    if n==1:
        return 4
    elif n>1:
        return 2*A(n-1)+3 
    else:
        return "input is not a positive integer!"
for n in range(1,6):
    print(A(n))