A = {1, 2, 3}
B = {1.5, 2, 2.5}
C = {4, 5, 6}

print('Объединение --------------------')
print('A | B', A | B)
print('A | C', A | C)
print("B | C", B | C)
print("A | B | C", A | B | C)

print('Пересечение ----------------')
print("A & B", A & B)
print('A & C', A & C)
print('B & C', B & C)
print('A & B & C', A & B & C)

print(' Разность ---------------')
print('A - B', A - B)
print('B - A', B - A)
print('A - C', A - C)
print('C - A', C - A)
print('B - C', B - C)
print('C - B', C - B)
print('A - B - C', A - B - C)
print('A - C - B', A - C - B)
print('B - A - C', B - A - C)
print('B - C - A', B - C - A)
print('C - A - B', C - A - B)
print('C - B - A', C - B - A)

print(' Симметрическая разность ------------')
print('A ^ B', A ^ B)
print('A ^ C', A ^ C)
print('B ^ C', B ^ C)
print('A ^ B ^ C', A ^ B ^ C)
