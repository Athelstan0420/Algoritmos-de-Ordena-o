Teoria = https://www.freecodecamp.org/portuguese/news/algoritmos-de-ordenacao-explicados-com-exemplos-em-python-java-e-c/



##
-> InsertionSort = Compara o elemento CHAVE com elementos anteriores;

-> Site = https://www.w3schools.com/dsa/dsa_algo_insertionsort.php

-> YouTube = https://www.youtube.com/watch?v=UBg3nJrGOKg&t=359s&pp=ygUVaW5zZXJ0aW9uIHNvcnQgcHl0aG9u

-> Exercicios = Insertion_sort = https://www.univates.br/roau/download/195/exercicios/Exerc_insertion.htm

-> Código em Python:

    import random  
    def insertion_sort(v):
        i = 1
        while i < len(v):
            temp = v[i]
            trocou = False            
            h = i - 1            
            while h >= 0 and v[h] > temp:            
                v[h + 1] = v[h]                
                trocou = True                 
                h -= 1                
            if trocou:            
                v[h+1] = temp              
            i += 1
      
    vetor = list(range(0,10))
    random.shuffle(vetor)
    insertion_sort(vetor)
    print(vetor)

##

##
-> SelectionSort = Percorre a array e seleciona o menor valor, realocando-o para 
o inicio da array; 

EX: seleciona o menor elemento e o coloca na posição 0 e assim sucessivamente. 

-> Site = https://www.w3schools.com/dsa/dsa_algo_selectionsort.php

-> YouTube = https://www.youtube.com/watch?v=SU4p59wFDSU&list=PLS_pKInUulqNChDCRu_QmjXX4s-WYGqzw&index=2

-> Código em Python:





##

