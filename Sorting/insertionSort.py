def insertionSort(L: list) -> list:
    S = [L[0]]
    U = list(L[1:])

    while len(U) > 0:
        print(S, U)
        idx = -1
        for j in range(len(S)):
            if U[0] < S[j]:
                idx = j
                break
        
        if idx == 0:
            S = [U[0]] + S
        elif idx < 0:
            S += [U[0]]
        else:
            S = S[:j] + [U[0]] + S[j:]
        
        U = U[1:]

    return S

x = [1,3,5,2,4,6]
print(insertionSort(x))


