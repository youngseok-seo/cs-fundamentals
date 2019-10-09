def mergeSort(L: list) -> list:
    if len(L) <= 1:
        return L

    split = (len(L)//2)
    a = mergeSort(L[:split])
    b = mergeSort(L[split:])

    L = merge(a, b)
    return L

def merge(a: list, b: list) -> list:
    leftIdx = 0
    rightIdx = 0
    mSorted = []
    for i in range(len(a) + len(b)):
        if leftIdx >= len(a) or b[rightIdx] < a[leftIdx]:
            mSorted += [b[rightIdx]]
            rightIdx += 1
        else:
            mSorted += [a[leftIdx]]
            leftIdx += 1

    return mSorted
        
x = [3,5,4,6,7,8,1,0,9]
print(mergeSort(x))