def NachatRabotu():
    print("Начало работы")

def SdelatStackPustym(S: list) -> None:
    S[0] = 0

def StackPust(S: list) -> bool:
    return S[0] == 0

def StackNePust(S: list) -> bool:
    return S[0] != 0

def EstSvobodnoeMesto(S: list, N: int) -> bool:
    return S[0] < N

def NetSvobodnogoMesta(S: list, N: int) -> bool:
    return S[0] >= N

def DobavitVStack(S: list, N: int, element: int) -> None:
    if NetSvobodnogoMesta(S, N):
        raise Exception("Переполнение стека")

    S[0] += 1
    S[S[0]] = element

def DostatIzStacka(S: list) -> int:
    if StackPust(S):
        return
    
    S[0] -= 1

    return S[S[0]+1]

def VershinaStacka(S: list) -> int:
    if StackPust(S):
        return
    return S[S[0]]

def UdalitIzStacka(S: list) -> None:
    if StackNePust(S):
        S[0] -= 1