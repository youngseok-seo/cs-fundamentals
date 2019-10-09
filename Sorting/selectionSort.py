def selectionSort(L: list) -> list:
    for i in range(len(L)):
        smallest = 999999
        for j in range(i, len(L)):
            if L[j] < smallest:
                smallest = L[j]
                sIdx = j
        sort = L[sIdx]
        L[sIdx] = L[i]
        L[i] = sort

        print(L)

    return L

x = [3,1,2,6,0, 8, 5]
print(selectionSort(x))