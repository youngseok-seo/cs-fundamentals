import sys
sys.path.append("../")

from Heap.heap import minHeap

def heapSort(L: list) -> list:
    if len(L) == 0:
        return []

    heap = minHeap()
    for num in L:
        heap.addElement(num)

    heapSorted = []
    while heap.length > 0:
        heapSorted += [heap.removeElement()]

    return heapSorted

# x = [99, -1, 7,4,6,2,3,8, 4]

# print(heapSort(x))


    





