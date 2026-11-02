from module import *

N = 5

S1 = [PROBEL for i in range(N+1)]
SdelatStackPustym(S1)

S2 = [PROBEL for i in range(N+1)]
SdelatStackPustym(S2)

DobavitVStack(1)
DobavitVStack(2)
DobavitVStack(3)
DobavitVStack(4)
DobavitVStack(5)

print(S1)
print(S2)

while StackNePust(S1):
    DobavitVStack(S2, N, DostatIzStacka(S1))

print(S1)
print(S2)