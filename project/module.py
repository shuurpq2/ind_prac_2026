global PUSTOY_SIMVOL
PUSTOY_SIMVOL = " "

def massiv_pust(massiv: list) -> bool:
    return massiv[0] == 0

def massiv_pust_s_proverkoy(massiv: list, dlina: int) -> bool:
    otvet = True

    for i in range(1, dlina+1):
        if massiv[i] != PUSTOY_SIMVOL:
            otvet = False
            break

    return otvet

def sdelat_massiv_pustym(massiv: list) -> list:
    massiv_copy = massiv.copy()

    for i in range(1, massiv_copy[0]+1):
        massiv_copy[i] = PUSTOY_SIMVOL
    massiv_copy[0] = 0

    return massiv_copy