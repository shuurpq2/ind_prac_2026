from module import *

def TestNachatRabotu():
    NachatRabotu() # Вызываем проверяемую функцию

TestNachatRabotu()

def TestSdelatStackPustym():
    N = 10
    S = [" "] * (N+1) # Создаем ряд длиной N+1 для возможности индексации от 1 до N
    S[0] = 1 # Ставим служебный элемент в значение 1 и заполняем стек
    S[1] = 3

    print(f"Изначальная длина стека: {len(S)}")

    SdelatStackPustym(S)

    print(f"Новая длина стека: {len(S)}")
    print(f"Значение служебного элемента: {S[0]}")

TestSdelatStackPustym()