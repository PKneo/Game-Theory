import nashpy as nash
import numpy as np
P1=np.array([[-1,-3],[0,-2]])
P2=np.array([[-1,0],[-3,-2]])
prisoner_dilemma=nash.Game(P1,P2)
prisoner_dilemma
eqs = prisoner_dilemma.support_enumeration()

#Handling readeble output
strategies = ["Cooperate", "Defect"]

for sigma_row, sigma_col in eqs:
    p1_choice = strategies[np.argmax(sigma_row)]
    p2_choice = strategies[np.argmax(sigma_col)]

    print(f"P1 chooses {p1_choice}, P2 chooses {p2_choice}")