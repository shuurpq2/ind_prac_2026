global PROBEL
PROBEL = " "

def SdelatMnozhestvoPustym(M: list) -> None:
    M[0] = 0

def MnozhestvoPusto(M: list) -> bool:
    return M[0] == 0

def MnozhestvoNePusto(M: list) -> bool:
    return M[0] != 0