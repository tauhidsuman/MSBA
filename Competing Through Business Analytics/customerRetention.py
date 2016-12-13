#VJ Davey
#customer retention
import numpy as np 

P = np.array([[0.5,0.5,0.0,0.0,0.0],[0.45,0.0,0.55,0.0,0.0],[0.4,0.0,0.0,0.6,0.0],[0.35,0.0,0.0,0.0,0.65],[0.25,0.0,0.0,0.0,0.0]])
I = np.array([[1.0,0.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0,0.0],[0.0,0.0,1.0,0.0,0.0],[0.0,0.0,0.0,1.0,0.0],[0.0,0.0,0.0,0.0,1.0]])
c = np.array([[1.0],[1.0],[1.0],[1.0],[1.0]])
L = np.linalg.inv(I-P)
L = np.dot(L,c)
print L