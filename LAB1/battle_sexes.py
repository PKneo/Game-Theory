import nashpy as nash
import numpy as np

#Creating matrixes
P1=np.array([[3,0],[0,2]])
P2=np.array([[2,0],[0,3]])

#Computing using Nashpy
battle_sexes=nash.Game(P1,P2)
eqs = list(battle_sexes.support_enumeration())

#Output
print("Array format output:", eqs)