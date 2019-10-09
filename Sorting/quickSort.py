def quickSort(L: list, m: int, n: int) -> list:
    if m < n:
        i = m
        j = n
        partition(L, i, j)
        quickSort(L, m, j)
        quickSort(L, i, n)

    return L

def partition(L: list, i: int, j: int) -> bool:
    pivot = L[(i + j)//2]
    while i <= j:
        while L[i] < pivot:
            i += 1
        while L[j] > pivot:
            j -= 1
        if i <= j:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
            i += 1
            j -= 1
    return True

x = [4,7,3,9,8,5,6,20]

print(quickSort(x, 0, 7))