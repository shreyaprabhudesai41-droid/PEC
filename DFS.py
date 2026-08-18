graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbours = input("Enter neighbours: ").split()
    graph[node] = neighbours

start = input("Enter starting node: ")

stack = [start]
visited = []

while stack:
    current = stack.pop()

    if current in visited:
        continue

    visited.append(current)
    print(current, end=" ")

    for x in reversed(graph.get(current, [])):
        if x not in visited:
            stack.append(x)

print("\nDFS:", visited)