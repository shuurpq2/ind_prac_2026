from module import *

def test_massiv_pust():
    N = 10  # Длина массива
    massiv = [PUSTOY_SIMVOL] * (N+1) # Создание массива длины N+1. +1 для возможности индексации от 1 до N
    massiv[0] = 0 # Выставление значения служебного элемента в 0

    assert massiv_pust(massiv) # Проверка: является ли массив пустым
    assert len(massiv) == N+1 # Проверка: осталась ли длина массива прежней
    print("Проверка с пустым массивом пройдена")

    massiv[0] = 1 # Выставление служебного элемента в значение 1

    assert not massiv_pust(massiv) # Проверка: является ли массив не пустым
    print("Проверка с не пустым массивом пройдена")

test_massiv_pust()

def test_massiv_pust_s_proverkoy():
    N = 10  # Длина массива
    M = 10
    massiv = [PUSTOY_SIMVOL] * (N+1) # Создание массива длины N+1. +1 для возможности индексации от 1 до N
    massiv[0] = 0 # Выставление значения служебного элемента в 0

    assert massiv_pust_s_proverkoy(massiv, N) # Проверка: является ли массив пустым
    assert N == M # Проверка: осталось ли значение N тем же самым
    assert len(massiv) == N+1 # Проверка: осталась ли длина массива прежней
    print("Проверка с пустым массивом пройдена")

    massiv[1] = "f" # Заполнение первого элемента массива
    massiv[0] = 1 # Изменение служебного элемента

    assert not massiv_pust_s_proverkoy(massiv, N)
    print("Проверка с не пустым массивом пройдена")

test_massiv_pust_s_proverkoy()

def test_sdelat_massiv_pustym():
    N = 10
    massiv = [PUSTOY_SIMVOL] * (N+1)

    massiv[1] = "f" # Заполнение массива и изменение служебного элемента
    massiv[2] = "a"
    massiv[0] = 2

    massiv = sdelat_massiv_pustym(massiv) # Вызов функции очистки

    assert len(massiv) == N+1 # Проверки на неизменность длины и пустоту массива
    assert massiv[0] == 0
    assert massiv[1] == massiv[2] == PUSTOY_SIMVOL
    print("Проверка очистки массива пройдена")

test_sdelat_massiv_pustym()