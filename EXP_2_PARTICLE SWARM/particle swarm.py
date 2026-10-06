import random

def cost(x):
    solar, wind = x
    demand = 100
    renewable = solar + wind
    backup = max(0, demand - renewable)

    return 2*solar + 3*wind + 8*backup

n = 20
iterations = 50
w = 0.7
c1 = 1.5
c2 = 1.5

particles = []
for _ in range(n):
    x = [random.uniform(0, 100), random.uniform(0, 100)]
    v = [random.uniform(-10, 10), random.uniform(-10, 10)]
    particles.append([x, v, x[:], cost(x)])

gbest = min(particles, key=lambda p: p[3])[2][:]

for _ in range(iterations):
    for p in particles:
        x, v, pbest, _ = p

        for i in range(2):
            r1 = random.random()
            r2 = random.random()

            v[i] = (w * v[i] +
                    c1 * r1 * (pbest[i] - x[i]) +
                    c2 * r2 * (gbest[i] - x[i]))

            x[i] += v[i]
            x[i] = max(0, min(100, x[i]))

        f = cost(x)

        if f < cost(pbest):
            pbest[:] = x[:]

        if f < cost(gbest):
            gbest[:] = x[:]

print("Optimal Renewable Integration")
print("Solar Power :", round(gbest[0], 2), "MW")
print("Wind Power :", round(gbest[1], 2), "MW")
print("Total Cost :", round(cost(gbest), 2))
