
def add_edge(my_dict: list[list], a: str, neighbor: list):
    my_dict[a] = neighbor

def bfs(graph: dict, start: str, goal: str) -> list:
    bfs: list = []
    visited: set = set()
    stack = [start]
    path_found = [goal]
    while stack:
        current = stack.pop(0)
        if current is goal:
            while current != start:
                current = bfs.pop()
                path_found.append(current)
            return path_found
        if current not in visited:
            visited.add(current)
            bfs.append(current)
            for neighbor in graph[current]:
                stack.append(neighbor)

    return bfs


if __name__ == "__main__":
    my_dict = {}
    add_edge(my_dict, "start", ["a","b"])
    add_edge(my_dict, "a", ["start", "Goal"])
    add_edge(my_dict, "b", ["start", "c", "e"])
    add_edge(my_dict, "c", ["b", "d"])
    add_edge(my_dict, "e", ["b", "d"])
    add_edge(my_dict, "d", ["c", "e", "Goal"])
    add_edge(my_dict, "Goal", ["a", "d"])
    print(my_dict)
    print(bfs(my_dict, "start", "Goal"))
