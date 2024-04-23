#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
N = 10000
s = 9999
i = 1
r = 0
beta = 0.3
gamma = 0.05
colors = ['b','c','g','m','r','w','y','slateblue','deeppink','maroon','darkmagenta']
V = [0,10,20,30,40,50,60,70,80,90,100]
S = [s]
I = [i]
R = [r]
T = [0]
#start a figure
plt.figure(figsize=(6,4),dpi=150)
# for different vaccination rate, reset the value of s
for i in range(11):
    s = 9999 * (100-V[i]) * 0.01
    i = 1
    r = 0
    for j in range(1,1000):
        #loop for 1000 days
        #infected people recover
        r += sum(np.random.choice(range(2),i,p=[1-gamma, gamma]))
        i -= sum(np.random.choice(range(2),i,p=[1-gamma, gamma]))
        #suspectible people be infected
        i += sum(np.random.choice(range(2),int(s),p=[1-beta*i/N, beta*i/N]))
        s -= sum(np.random.choice(range(2),int(s),p=[1-beta*i/N, beta*i/N]))
        #append all numbers updated into lists
        S.append(s)
        I.append(i)
        R.append(r)
        T.append(j)
    plt.plot(T,I,label=str(V[i])+'%',c=colors[i])

plt.legend()
plt.show()
plt.clf()