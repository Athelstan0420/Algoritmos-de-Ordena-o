# ALGORITMOS DE ORDENAÇÃO:
"""
Instruções que recebem uma lista ou um
vetor como entrada e organiza os itens 
em uma ordem específica.
"""

# Insertion sort:
"""
Insertion sort = Compara o elemento CHAVE
com os elementos anteriores, se o elemento 
anterior > elemento chave você move esse
elemento anterior para próxima posição.

* COMECE DO ÍNDICE 1. *

"""

# Biblioteca "aleatório":
import random
# Biblioteca "tempo"
import time

# Função:
# O paramentro 'v' é o vetor_array;
def insertion_sort(v):
    indice_atual = 1 # CHAVE
    """
    enquanto o indice atual for menor que o 
    tamanho do vetor_array, LOOP ABAIXO:
    """
    while indice_atual < len(v):
        """
        O valor do indice_atual será armazenado em
        uma variável temporária. Já que o indice
        irá ser trocado. ABAIXO:
        """
        var_temp = v[indice_atual]
        
        """
        Se eu realizar alguma troca, a 
        variável 'trocou' passa a ser "True", mas
        se incia como FALSE.
        ABAIXO:
        """
        trocou = False
        
        """
        Elemento anterior ao indice atual,
        ou seja, com quem o indice atual
        irá se comparar. ABAIXO:
        """
        elem_anterior = indice_atual - 1
        
        """
        Enquanto o elem_anterior >= 0 e 
        elem_anterior > valor do indice atual
        ABAIXO:
        """
        while elem_anterior >= 0 and v[elem_anterior] > var_temp:
            """
            é somado um indice há posição do elemento anterior
            ABAIXO:
            """
            v[elem_anterior + 1] = v[elem_anterior]
            """
            Se trocou, então é True
            """
            trocou = True
            elem_anterior -= 1
        if trocou:
            v[elem_anterior+1] = var_temp
        indice_atual += 1            
        
"""
ABAIXO: Vetor que possui uma lista com números
no intervalo de 0 á 10:
"""
vetor_array = list(range(0,1000))

# Método 'shuffle' = embaralhar
random.shuffle(vetor_array) 

antes = time.time() # Calcular desempenho

# Chamar função Insertion_sort()
insertion_sort(vetor_array)

depois = time.time() # Calcular desempenho
# cauculando o desempenho
total = (depois - antes) * 1000

print(vetor_array)
# tempo gasto para realizar tarefa, ABAIXO:
print(f" Tempo gasto para realizar tarefa foi: {total} ms")