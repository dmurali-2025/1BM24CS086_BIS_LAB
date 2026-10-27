import random

def objective(x):
    return x * x

N = 10
T = 50
rho = 0.5
Q = 100

values = list(range(-5, 6))
pheromone = [1.0] * len(values)

best_solution = None
best_cost = float('inf')

for iteration in range(T):
    ants = []

    for ant in range(N):
        total = sum(pheromone)
        r = random.uniform(0, total)
        cumulative = 0

        for i in range(len(values)):
            cumulative += pheromone[i]

            if cumulative >= r:
                x = values[i]
                break

        cost = objective(x)
        ants.append([x, cost])

        if cost < best_cost:
            best_cost = cost
            best_solution = x

    for i in range(len(pheromone)):
        pheromone[i] *= (1 - rho)

    for ant in ants:
        index = values.index(ant[0])
        deposit = Q / (1 + ant[1])
        pheromone[index] += deposit

print("Best Solution:", best_solution)
print("Minimum Function Value:", best_cost)
