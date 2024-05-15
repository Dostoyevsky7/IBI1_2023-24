# What does this piece of code do?
# Answer:
#pick a random number between 1 and 10 for 100 times and calculate their sum
# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
total_random_number=0
while progress<100: ###pre set that this while loop would run for 100 times
	progress+=1
	n = randint(1,10)
	total_random_number = total_random_number+n ###add every number together

print(total_random_number)
