# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
N = 10000
s = 9999
i = 1
r = 0
beta = 0.3
gamma = 0.05
S = [s]
I = [i]
R = [r]
time = [0]
for j in range (1,1001):
    time.append(j)
    #pick random infected individuals and they will recover
    recov = sum(np.random.choice(range(2),i,p=[1-gamma, gamma]))
    r += recov
    R.append(r)
    i -= recov
    #pick random suspectible individuals and they will be infected
    infect = sum(np.random.choice(range(2), s, p=[1-beta*i/N, beta*i/N]))
    i += infect
    I.append(i)
    s -= infect
    S.append(s)
plt.figure(figsize = (6,4), dpi = 150)
plt.plot(time, S, label = 'Suspectible', color = 'blue')
plt.plot(time, I, label = 'Infected', color = 'yellow')
plt.plot(time, R, label = 'Recovered', color = 'green')
plt.title('SIR model')
plt.xlabel('time')
plt.ylabel('number of people')
plt.show()
plt.clf()