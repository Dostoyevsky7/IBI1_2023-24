# use for loop: pre-set 5 times of calculations
a=4
print(a)###how to include a=4 i and print out in the loop?
for i in range (1,5):
    a=2*a+3
    print(a)

# use while loop: make the final value is 109
a=4
print(a) #why cant involve the initial a into the loop?
while a<109: #attention this is < not <=!!! because if <=, 109 would satisfy the loop again
    a=2*a+3
    print(a)