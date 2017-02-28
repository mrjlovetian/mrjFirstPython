import matplotlib.pyplot as plt

from random_walk import RandomWalk 

#创建一个randomwlak实例，并将包含的点绘制出来
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s = 15)
plt.show()