
from random import shuffle
vetor = list(range(0,10))
shuffle(vetor)
print(vetor)

i = 0
while i < len(vetor) - 1:
    menor = i
    sucessor = i + 1
    while sucessor < len(vetor):
        if vetor[sucessor] < vetor[menor]:
            menor = sucessor
        sucessor += 1
    if menor != i:
        temp = vetor[i]
        vetor[i] = vetor[menor]
        vetor[menor] = temp
    i+=1


print(vetor)


