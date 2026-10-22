global PROBEL
PROBEL = " "

def SdelatMnozhestvoPustym(M: list) -> None:
    M[0] = 0

def MnozhestvoPusto(M: list) -> bool:
    return M[0] == 0

def MnozhestvoNePusto(M: list) -> bool:
    return M[0] != 0

def EstSvobodnoeMesto(M: list, N: int) -> bool:
    return M[0] < N

def NetSvobodnogoMesta(M: list, N: int) -> bool:
    return M[0] >= N

def ElementPrinadlezhitMnozhestvu(M: list, element: int) -> bool:
    otvet = False

    for i in range(1, M[0]+1):
        if M[i] == element:
            otvet = True
            break

    return otvet

def ElementNePrinadlezhitMnozhestvu(M: list, element: int) -> bool:
    otvet = True

    for i in range(1, M[0]+1):
        if M[i] == element:
            otvet = False
            break

    return otvet