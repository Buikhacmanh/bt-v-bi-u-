import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
y = x**3
divisions = ["Div-A","Div-B","Div-C","Div-D","Div-E"]
divisions_average_marks = [70,82,73,65,68]

plt.bar(divisions, divisions_average_marks, color = 'blue')
plt.title("bar graph")
plt.xlabel("divisions")
plt.ylabel("marks")
plt.show()