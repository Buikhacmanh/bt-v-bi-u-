import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4,5],[1,4,9,16,20],"go")
plt.title("1st subplot")

plt.subplot(1,2,2)
plt.plot(x,y,"r^")
plt.title("2nd subplot")

plt.suptitle("My sub-plost")
plt.show()