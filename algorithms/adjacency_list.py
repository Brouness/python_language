from python_language.algorithms.bfs_algo_dict import bfs

def add_edge(my_dict: list[list], a: str, neighbor: list):
    my_dict[a] = neighbor

if __name__ == "__main__":
    my_dict = {}
    add_edge(my_dict, "start", ["a","b"])
    add_edge(my_dict, "a", ["start", "b", "Goal"])
    add_edge(my_dict, "b", ["start", "a"])
    print(my_dict)
    path = bfs(my_dict, "start", "Goal")
    print(path)