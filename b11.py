import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
y = x**3
firms = ["Div-A","Div-B","Div-C","Div-D","Div-E"]
market_share = [20,25,15,10,20]
explode = [0,0.1,0,0,0]
plt.pie(market_share,explode=Explode,labels=firms, shadow=true,startangle=45)
plt.axis('equal')
plt.legend(title="tron")
plt.show()