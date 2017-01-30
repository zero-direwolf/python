from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

x,y=np.loadtxt('ex1data1.txt',
	             unpack=True,
	             delimiter=',')
plt.plot(x,y,'k+')
plt.title('ml chart')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()
plt.grid(True,color='r')