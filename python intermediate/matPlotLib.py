from matplotlib import pyplot as plt

x=[5,2,6,8,7,4]
y=[6,2,5,8,8,6]
print(len(x))
print(len(y))
plt.plot(x,y,'rx')
plt.title('new chart')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.grid(True,color='k')
plt.show()