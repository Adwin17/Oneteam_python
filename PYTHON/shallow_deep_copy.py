import copy
L=["Adwin",[17,2008],"Kochi"]

K=L
print(K)
print(L)

P=copy.copy(L)
P[1][0]=20

print(P)

O=copy.deepcopy
print(O)
