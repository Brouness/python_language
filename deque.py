from collections import deque
from heapq import heapify, heappop


if __name__ == "__main__":
    d = deque([1, 2, 3])
    # add a item
    d.append(4)
    # add in front
    d.appendleft(15)
    d.rotate(2)
    print(d)
    lis = list(d)
    heapify(lis)
    print(lis)
    print(d)
