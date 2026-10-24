from heapq import heapify, heappop


if __name__ == "__main__":
    li = [25,24,23,28]
    heappop(li)
    print(li[-4:])
    heapify(li[-1:])
    print("Heap queue:", li)
