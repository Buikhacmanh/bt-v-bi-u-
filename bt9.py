import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
y = x**3
divisions = ["Div-A","Div-B","Div-C","Div-D","Div-E"]
girl_average_marks = [70,82,73,65,68]
boys_average_marks = [68,87,50,45,88]

index = np.arange(5)
width = 0.30

plt.bar(index, divisions_average_marks, width, color = 'blue',label = 'boy')
plt.bar(index, boys_average_marks, width, label = 'girl', color = 'red',bottom= girl_average_marks)
plt.title("bar graph")
plt.ylabel("divisions")
plt.xlabel("marks")
plt.xticks(index, divisions)

plt.legend(loc = 'best')
plt.show()