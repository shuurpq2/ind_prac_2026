from module import *

N = 5

S1 = [0 for i in range(N+1)]
SdelatStackPustym(S1)

S2 = [0 for i in range(N+1)]
SdelatStackPustym(S2)

DobavitVStack(S1, N, 1)
DobavitVStack(S1, N, 2)
DobavitVStack(S1, N, 3)
DobavitVStack(S1, N, 4)
DobavitVStack(S1, N, 5)

print(f"Стек 1 до переноса: {S1}")
print(f"Стек 2 до переноса: {S2}")

while StackNePust(S1):
    DobavitVStack(S2, N, DostatIzStacka(S1))

print(f"Стек 1 после переноса: {S1}")
print(f"Стек 2 после переноса: {S2}")