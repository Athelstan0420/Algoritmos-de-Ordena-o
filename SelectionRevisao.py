from random import shuffle

def selection_sort(v):
    i = 0 
    while i < len(v) - 1:
        m = i
        j = i+1
        while j < len(v):
            if v[j] < v[m]:
                m = j
            j+=1
        if m != i:
            t = v[i]
            v[i] = v[m]
            v[m] = t
        i+=1
vetor = list(range(0,10))
shuffle(vetor)
selection_sort(vetor)
print(vetor)