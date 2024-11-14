import numpy as np
import matplotlib.pyplot as plt

#hi arshad, comments below to help you understand

#define xdot and ydot in these functions, use np.sin(x)
#and np.cos(x) for sin/cos, they take arguments in radians
def dxdt(x,y):
    return y

def dydt(x,y):
    return -x-(x*x+y*y-1)*x

w=4 #just a parameter
#the 1000 is the resolution, i think you can keep it the same
#change the -w and w below to whatever you like, they control the
#y axis and x axis limits
Y,X=np.mgrid[-w:w:1000j,-w:w:1000j]
U,V=dxdt(X,Y),dydt(X,Y) #creates the vectors
fig,axs=plt.subplots() #creates the plot
#creates a streamplot from X,Y,U,V
#also density controls how dense the plot is
axs.streamplot(X,Y,U,V,density=3)
plt.tight_layout()
plt.show()


