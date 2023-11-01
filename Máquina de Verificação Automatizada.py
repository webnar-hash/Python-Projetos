lista1 = []
lista2 = []
data = []

for l in range(0, 6):
    lista1.append(int(input()))
    
for x in range (0, 6):
    lista2.append(int(input()))
    
for i in range (0, 6):    
    if lista1[i] == lista2[i]:
        data.append(False)
        
    elif lista1[i] != lista2[i]:
        data.append(True)
    
if all(data) == True:
    print('Y')
else:
    print('N')
        

