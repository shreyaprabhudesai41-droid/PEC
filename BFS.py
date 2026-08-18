graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    graph[node] = input("Enter neighbours: ").split()

start = input("Enter starting node: ")

queue = [start]
visited = []

while queue:
    current = queue.pop(0)

    if current in visited:
        continue

    visited.append(current)
    print(current, end=" ")

    neighbours = graph.get(current, [])

    for x in neighbours:
        if x not in visited:
            queue.append(x)

print("\nBFS:", visited)