#define a function to calculate the number of chocolate bar the user can afford
def choc(x, y):
    money = float(x)
    c_price = float(y)
    number = int(money // c_price)
    change = money - number*c_price
    return(number, change)
t_money = input('Total money you have is: ')
choc_p = input('The price of the chocolate br is: ')
result = choc(t_money, choc_p)
#the result is (number, change), extract them separately and print out
print('You can buy ', result[0], 'chocolate bars and you will have', result[-1], 'for change')