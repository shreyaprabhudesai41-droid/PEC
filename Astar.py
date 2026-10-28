graph = {
    'A': {'B': 5, 'C': 6, 'D': 4},
    'B': {'E': 4, 'C': 2},
    'E': {'G': 1},
    'C': {'F': 4},
    'D': {'C': 3, 'I': 6},
    'I': {},
    'F': {},
    'G': {}
}

h = {'A': 6, 'B': 2, 'C': 4, 'D': 4,
     'E': 1, 'F': 5, 'G': 0, 'I': 5}


def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]
    closed = []

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", g)
            return

        if node in closed:
            continue

        closed.append(node)

        for child, cost in graph[node].items():
            if child not in closed:
                new_g = g + cost
                new_f = new_g + h[child]

                open_list.append(
                    (new_f, new_g, child, path + [child])
                )

    print("Path not found")


astar('A', 'G')