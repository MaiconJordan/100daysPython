lista = [6,8,3,8,5,0,12,43,7,1,78,43,12,56,43,12,13,14,23,25,26,2]

#Algoritimo que ordena uma lista
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubble_sort(lista))

#função do proprio python que ordena uma lista
lista.sort()
print(lista)