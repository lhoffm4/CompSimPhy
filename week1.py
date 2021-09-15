import numpy as np
import matplotlib.pyplot as plt

x=np.array ([3,4,1])
y=np.array([1,0,2])
a= np.dot(x,y)
print(a)

A=[[1,2],[3,4]]
B=np.array(A)
print('a',A+A)
print('b',B+B)
print('c',A+B)
#print('d',A-A)
print('e',B-B)
print('f',2*A)
print('g',2*B)
#print('h',A*A)
print('i',B*B)
print('j',np.dot(B,B))
print('k',B**2)
print('l',B/B)

x=np.array([range(1,11,1)])
y=x**2
print(y)
plt.plot(x,y,'.',x,y,'-')
plt.show()
