import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
y = x**3
divisions = ["Div-A","Div-B","Div-C","Div-D","Div-E"]
divisions_average_marks = [70,82,73,65,68]
boys_average_marks = [68,87,50,45,88]

index = np.arange(5)
width = 0.30

plt.bar(index, divisions_average_marks, width, color = 'blue',label = 'boy')
plt.bar(index+width, boys_average_marks, width, label = 'girl', color = 'red')
plt.title("bar graph")
plt.xlabel("divisions")
plt.ylabel("marks")
plt.xticks(index+ width/2, divisions)

plt.legend(loc = 'best')
plt.show()