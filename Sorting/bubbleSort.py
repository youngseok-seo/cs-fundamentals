def bubbLeSort(L: list) -> list:
    while True:
        swapped = False
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                smaller = L[j + 1]
                L[j + 1] = L[j]
                L[j] = smaller
                swapped = True
        if swapped == False:
            break

    return L
            
x = [4, 3, 5, 12, 9, 2]
print(bubbLeSort(x))