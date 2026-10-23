from collections import deque


def new_graph(verteces: list) -> dict:
    my_dict: dict = {}
    for vertex in verteces:
        my_dict[vertex] = set()
    return my_dict


def add_neighbor(graph: dict, a: str, b: str) -> None:
    graph[a].add(b)
    graph[b].add(a)


def bfs(graph, start: str) -> list:
    if start not in graph:
        print("start point not in graph")
        return []
    visited: dict = {}
    queue = deque([start])
    visited[start] = None
    bfs_reach: list = [start]
    while queue:
        front = queue.popleft()
        for city in graph[front]:
            if city not in visited:
                visited.add(city)
                queue.append(city)
                bfs_reach.append(city)
    return bfs_reach


if __name__ == "__main__":
    verteces: list = ["start", "a", "b", "Goal"]
    graph: dict = new_graph(verteces)
    add_neighbor(graph, "a", "b")
    add_neighbor(graph, "start", "a")
    add_neighbor(graph, "start", "b")
    add_neighbor(graph, "Goal", "a")
    print(graph)
    print(bfs(graph, "start"))
