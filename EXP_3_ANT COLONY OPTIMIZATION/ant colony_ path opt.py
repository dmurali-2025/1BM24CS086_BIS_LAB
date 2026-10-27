import random

graph = [
    [0, 2, 4, 7, 3],
    [2, 0, 1, 5, 6],
    [4, 1, 0, 2, 3],
    [7, 5, 2, 0, 1],
    [3, 6, 3, 1, 0]
]

n = len(graph)
ants = 10
iterations = 50
rho = 0.5
Q = 100

pheromone = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(1.0)
    pheromone.append(row)

best_path = []
best_cost = float('inf')

for iteration in range(iterations):
    paths = []

    for ant in range(ants):
        start = random.randint(0, n - 1)
        path = [start]
        visited = [False] * n
        visited[start] = True
        cost = 0
        current = start

        while len(path) < n:
            choices = []

            for j in range(n):
                if not visited[j]:
                    choices.append(j)

            total = 0

            for j in choices:
                total += pheromone[current][j] / graph[current][j]

            r = random.uniform(0, total)
            cumulative = 0
            next_city = choices[-1]

            for j in choices:
                cumulative += pheromone[current][j] / graph[current][j]
                if cumulative >= r:
                    next_city = j
                    break

            path.append(next_city)
            visited[next_city] = True
            cost += graph[current][next_city]
            current = next_city

        cost += graph[current][start]
        path.append(start)

        paths.append([path, cost])

        if cost < best_cost:
            best_cost = cost
            best_path = path[:]

    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= (1 - rho)

    for path, cost in paths:
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            pheromone[u][v] += Q / cost
            pheromone[v][u] += Q / cost

print("Best Path:", end=" ")
for city in best_path:
    print(city, end=" ")

print("\nMinimum Distance:", best_cost)
