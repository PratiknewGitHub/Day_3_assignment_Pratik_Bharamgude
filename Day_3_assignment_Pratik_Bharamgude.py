#1. Generate random data with NumPy for 1000 data points with 2 columns only.
#Ans-
import numpy as np
x = np.random.randint(1,1000,(20,2))
print(x)

#2. Plot Scatter plot, line plot with that in all variations we covered in the class.
#Ans-
import matplotlib.pyplot as plt
plt.scatter(dataset[0][0], dataset[0][1], c="red", s=50, label="From X1, Y1", marker="o", edgecolors="k")
plt.scatter(dataset[1][0], dataset[1][1], c="green", s=50, label="From X2, Y2", marker=
"^", edgecolors="y")
plt.title("Labelled data")
plt.xlabel("$X axis$")
plt.ylabel("$Y axis$")
plt.legend()
plt.show()

x = np.array([i*2 for i in range(1, 15)])
y1 = np.array([i*2 for i in range(1, 15)])
y2 = np.array([3, 6, 9, 12, 15, 18, 21, 24, 27, 30])
dataset = [(x, y1), 
           (x, y2)]
plt.plot(dataset[0][0], dataset[0][1], c="red",label="From X1, Y1", linestyle="dotted")
plt.plot(dataset[1][0], dataset[1][1], c="green", label="From X2, Y2", linestyle="dashed")
plt.title("Labelled lines")
plt.xlabel("$X-axis$")
plt.ylabel("$Y-axis$")
plt.legend()
plt.show()


