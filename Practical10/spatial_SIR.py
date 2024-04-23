# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#0 for S, 1 for I, 2 for R
#buld an array 100*100, all are suspectable
population = np.zeros((100,100))
#choose one random person to be the source of the outbreak
outbreak = np.random.choice(range(100),2)
population[outbreak[0], outbreak[1]] = 1
#plot a figure, the infected one is in yellow
plt.figure(figsize =(6,4), dpi = 150)
plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
#set up parameter
beta = 0.3
gamma = 0.05
plt.figure(figsize =(6,4), dpi = 150)
#loop for 100 times
for i in range(100):
    infect = np.where(population == 1)
    #infected people get recover
    for j in infect[0]:
        for k in infect[1]:
            population[j,k] = np.random.choice([1,2],1,p=[1-gamma, gamma])
    #infected people infect others
    for j in infect[0]:
        for k in infect[1]:
            for n in range(-1,2,1):
                if population[j+n, k+n] == 0:
                    population[j+n, k+n] = np.random.choice(range(2),1,p=[1-beta, beta])
    plt.title("at day"+str(i))
    plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')  
    plt.show()
plt.clf()