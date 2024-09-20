
"""
# Selection_Sort:

Percorre a array e seleciona o menor valor, realocando-o para 
o inicio da array;

EX: seleciona o menor elemento e o coloca na posição 0 e assim sucessivamente.
"""

import random

def selection_sort(v):
    # iniciando um contador, ABAIXO:
    i = 0 
    # Indica inicialmente o menor elemento:
    while i < len(v) - 1:
        """Sugerindo que o menor é quem está na 
        posição i, iniciando em na pos. 0, ABAIXO:"""
        menor = i
        """Número seguinte ao 'i', ABAIXO:"""
        j = i + 1
        # confirma o menor elemento:
        while j < len(v):
            """Se O valor que esta na posição 'J' for
            menor que o valor que está em 'vmenor' 
            o 'menor' recebe 'j'; ABAIXO:
            """
            if v[j] < v[menor]:
                menor =  j
            # 'j' anda uma casa, ABAIXO:   
            j += 1
        if menor != i:
            temp = v[i]
            v[i] = v[menor]
            v[menor] = temp
        i += 1

vetor= list(range (0, 10))
random.shuffle(vetor)
# selection_sort(vetor)
print(vetor)

