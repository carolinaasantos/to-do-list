# Vamos treinar o Insertionsort
# Dado um vetor [5, 2, 13, 7, -3, 4, 15, 10, 1, 6] vamos ordená-lo

def Insertionsort(L, n):
    iteracao = 0
    for i in range (1, n):
        k = i
        while k > 0 and L[k] < L[k-1]:
            aux = L[k]
            L[k] = L[k-1]
            L[k-1] = aux
            k = k-1
            iteracao += 1
    return iteracao

def Shellsort(L, n):
    h = n//2
    iteracao = 0
    while h > 0:
        for i in range (h, n):
            j = i
            while j >= h and L[j-h] > L[j]:
                aux = L[j]
                L[j] = L[j-h]
                L[j-h] = aux
                j = j - h
        h = h//2 # Na sequência de Shell
        iteracao += 1
    return iteracao


vetor = [5, 2, 13, 7, -3, 4, 15, 10, 1, 6]
vetor2 = [5, 2, 13, 7, -3, 4, 15, 10, 1, 6]

qntd = Insertionsort(vetor, len(vetor))
print('=== INSERTIONSORT ===')
print(f'Iteracoes: {qntd}')
print(vetor)
print('')

qntd2 = Shellsort(vetor2, len(vetor2))
print('=== SHELLSORT ===')
print(f'Iteracoes: {qntd2}')
print(vetor2)
print('')
print('Shellsort é mais eficiente')