contador = 0
lista = []

for i in range(0, 4):
      lista.append(input())

for x in range(0, 3):
    if lista[x] != lista[x+1]:
        contador += 1

print(contador)
    