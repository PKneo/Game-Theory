import nashpy as nash
import numpy as np

#Creating matrixes
P1=np.array([[1,-1],[-1,1]])
P2=np.array([[-1,1],[1,-1]])

#Computing using Nashpy
matching_pennies=nash.Game(P1,P2)
eqs = list(matching_pennies.support_enumeration())

#Output
print("Array format output:", eqs)