from collections import deque

if __name__ == "__main__":
    d = deque(['a', 'b', 'c'])
    # add a item
    d.append('d')
    # add in front
    d.appendleft("root")
    d.rotate(4)
    print(d)
