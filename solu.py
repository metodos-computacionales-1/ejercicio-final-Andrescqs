import numpy as np
import matplotlib.pyplot as plt 

datos = np.loadtxt("solu.dat")

t=datos[:,0]
Tht=datos[:,1]
w=datos[:,2]

plt.figure()
plt.plot(t, Tht)
plt.xlabel("t")
plt.ylabel("$\\theta$")
plt.title("$F_{d} = 1.4$")
plt.show()
plt.savefig("solu.png")