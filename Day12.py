import random

pipe_dict = {}

with open("Day12Input.txt", "r") as f:
    for line in f:
        current = line.split(" <-> ")
        pipe_dict[current[0]] = [i.strip() for i in current[1].strip().split(",")]


def recursive_dfs(graph, start, path=[]):
    """recursive depth first search from start"""
    path = path + [start]
    for node in graph[start]:
        if not node in path:
            path = recursive_dfs(graph, node, path)
    return path


total = 0
current = "0"
while True:
    group = recursive_dfs(pipe_dict, current)
    total += 1
    for item in group:
        del pipe_dict[item]
    if len(pipe_dict.keys()) == 0:
        break
    current = random.choice(list(pipe_dict.keys()))

print(total)
