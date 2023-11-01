caixa = [1.00, 10.00, 20.00, 50.00, 100.00]
saque = float(input())
cédulas = 0


for x in range (0, 11):
    if saque >= caixa[4]:
        saque -= caixa[4]
        cédulas += 1
    else:
        break

for w in range(0, 21):
    if saque >= caixa[3]:
        saque -= caixa[3]
        cédulas += 1
    else:
        break
        
for y in range(0, 21):
     if saque >= caixa[2]:
        saque -= caixa[2]
        cédulas += 1        
     else:
         break

for z in range(0, 51):
     if saque >= caixa[1]:
        saque -= caixa[1]
        cédulas += 1
     else:
         break
        
for p in range(0, 51):
     if saque >= caixa[0]:
        saque -= caixa[0]
        cédulas += 1
     else:
         break
    


print(f'total de cédulas de R$ 100.00 retiradas: {x}')
print(f'total de cédulas de R$ 50.00 retiradas: {w}')
print(f'total de cédulas de R$ 20.00 retiradas: {y}')
print(f'total de cédulas de R$ 10.00 retiradas: {z}')
print(f'total de cédulas de R$ 1.00 retiradas: {p}')
print(f'total de cédulas retiradas: {cédulas}')


        
    