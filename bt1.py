import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
y = x**3
divisions = ["Div-A","Div-B","Div-C","Div-D","Div-E"]
divisions_average_marks = [70,82,73,65,68]
variance = [5,7,5,8,9]

plt.barh(divisions, divisions_average_marks, xerr = variance, color = 'blue')
plt.title("bar graph")
plt.xlabel("marks")
plt.ylabel("divisions")
plt.show()