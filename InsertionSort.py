import random

vetor = list(range(0,5))

random.shuffle(vetor)

indice_atual = 1

while indice_atual < len(vetor):
    var_temp = vetor[indice_atual]
    trocou = False
    elem_anterior = indice_atual - 1

    while elem_anterior >= 0 and vetor[elem_anterior] > var_temp:
        vetor[elem_anterior + 1] = vetor[elem_anterior]
        trocou = True
        elem_anterior -= 1
        
    if trocou:
        vetor[elem_anterior + 1] = var_temp
    indice_atual += 1

print(vetor)


