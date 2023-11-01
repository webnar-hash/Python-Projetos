lista = {}
n = int(input())
porcentagem = 0

for i in range(n):
    
    arvore = input('selecione a arvore: ')
    
    if arvore == "":
        break
    
    elif lista.get(arvore):
        lista[arvore]
        
    else:
        lista[arvore] = 1
        porcentagem += 1

    for nome, valor in sorted(lista.items()):
        valor = 100 + (valor / porcentagem - 1) * 100
        print(f'{nome} {valor}')


