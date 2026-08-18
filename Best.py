graph = {}
h = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbours = input("Enter neighbours: ").split()
    graph[node] = neighbours
    h[node] = int(input("Enter heuristic value: "))

start = input("Enter starting node: ")
goal = input("Enter goal node: ")

open_list = [start]
visited = []

while open_list:
    current = open_list.pop(0)

    if current in visited:
        continue

    visited.append(current)
    print(current, end=" ")

    if current == goal:
        print("\nGoal found!")
        break

    for x in graph.get(current, []):
        if x not in visited:
            open_list.append(x)

    open_list.sort(key=lambda x: h.get(x, 999))

print("Best First Search:", visited)