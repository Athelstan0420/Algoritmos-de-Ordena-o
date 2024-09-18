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
