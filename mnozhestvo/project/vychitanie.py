from module import PROBEL, SdelatMnozhestvoPustym, DobavitVMnozhestvoElement, UdalitIzMnozhestva, DostatIzMnozhestva

NA = 4
A = [PROBEL] * (NA+1) # Создаем ряд A длиной NA+1 и заполняем
SdelatMnozhestvoPustym(A)
DobavitVMnozhestvoElement(A, 4)
DobavitVMnozhestvoElement(A, 2)
DobavitVMnozhestvoElement(A, 91)
DobavitVMnozhestvoElement(A, 89)

NB = 5
B = [PROBEL] * (NB+1) # Создаем ряд B длиной NB+1 и заполняем
SdelatMnozhestvoPustym(B)
DobavitVMnozhestvoElement(B, 7)
DobavitVMnozhestvoElement(B, 18)
DobavitVMnozhestvoElement(B, 33)
DobavitVMnozhestvoElement(B, 4)
DobavitVMnozhestvoElement(B, 2)

print(f"Множество A: {A}")
print(f"Множество B: {B}")

while B[0] > 0:
    UdalitIzMnozhestva(A, DostatIzMnozhestva(B, 1))

print(f"Результат вычитания B из A: {A}")