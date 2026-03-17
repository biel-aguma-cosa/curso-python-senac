A = int(input('numero: '))

B = 1
for i in range(A):
    B *= i+1
print(f'{A}! = {B}')