#to determine someone's favourite James Bond
#deine a function, the birth year metched with different Bonds
def f_Bond(x):
    r = 'Roger Moore'
    t = 'Timothy Dalton'
    p = 'Pierce Brosnan'
    d = 'Daniel Craig'
    if 1973 <= (x+18) <= 1986:
        f = r
    elif (x+18) <= 1994:
        f = t
    elif (x+18) <= 2005:
        f = p
    elif (x+18) <= 2021:
        f = d
    return f
#example: if the person was bron in 1981
print(f_Bond(1981))
#the user can put any year they were born
b_year = int(input("the year you were born:"))
print("Your favourite James Bond is: ", f_Bond(b_year))