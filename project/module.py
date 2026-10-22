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

def UdalitIzMnozhestva(M: list, element: int) -> None:
    udalen_index = 0

    for i in range(1, M[0]+1):
        if M[i] == element:
            M[i] = PROBEL
            udalen_index = i
            break

    if udalen_index < 1: return

    for i in range(udalen_index+1, M[0]+1):
        M[i-1] = M[i]
        M[i] = PROBEL

    M[0] -= 1

def DobavitVMnozhestvoElement(M: list, element: int) -> None:
    if ElementPrinadlezhitMnozhestvu(M, element): return

    M[0] += 1
    M[M[0]] = element

def ObjedinitMnozhestva(M1: list, M2: list) -> list:
    R = [PROBEL] * (M1[0] + M2[0] + 1)
    R[0] = 0

    for i in range(1, M1[0]+1): DobavitVMnozhestvoElement(R, M1[i])
    for i in range(1, M2[0]+1): DobavitVMnozhestvoElement(R, M2[i])

    return R[:R[0]+1]