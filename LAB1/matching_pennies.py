import nashpy as nash
import numpy as np

#Creating matrixes
P1=np.array([[1,-1],[-1,1]])
P2=np.array([[-1,1],[1,-1]])

#Computing using Nashpy
prisoner_dilemma=nash.Game(P1,P2)
prisoner_dilemma

eqs = list(prisoner_dilemma.support_enumeration())

#Output
print("Array format output:", eqs)