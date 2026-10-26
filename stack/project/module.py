def NachatRabotu():
    print("Начало работы")

def SdelatStackPustym(S: list) -> None:
    S[0] = 0

def StackPust(S: list) -> bool:
    return S[0] == 0

def StackNePust(S: list) -> bool:
    return S[0] != 0

def DobavitVStack(S: list, N: int, element: int) -> None:
    if S[0] == N:
        raise Exception("Переполнение стека")

    S[0] += 1
    S[S[0]] = element