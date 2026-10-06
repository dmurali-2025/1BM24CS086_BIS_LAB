import random
import time

N = 5
POP = 10
GEN = 50

burst = [6, 2, 8, 3, 4]
def fitness(s):
    wait = 0
    time = 0
    for i in range(N):
        wait += time
        time += burst[s[i]]
    return wait
def shuffle(s):
    random.shuffle(s)
def mutate(s):
    if random.randint(0, 9) == 0:
        i = random.randrange(N)
        j = random.randrange(N)

        t = s[i]
        s[i] = s[j]
        s[j] = t
def main():
    random.seed()
    p = [[0] * N for _ in range(POP)]
    newp = [[0] * N for _ in range(POP)]
    for i in range(POP):
        for j in range(N):
            p[i][j] = j
        shuffle(p[i])
    for g in range(GEN):
        best = 0
        for i in range(1, POP):
            if fitness(p[i]) < fitness(p[best]):
                best = i
        print("Generation", g + 1,
              ": Waiting Time =", fitness(p[best]))
        for j in range(N):
            newp[0][j] = p[best][j]
        for i in range(1, POP):
            a = random.randrange(POP)
            b = random.randrange(POP)
            parent = a if fitness(p[a]) < fitness(p[b]) else b
            for j in range(N):
                newp[i][j] = p[parent][j]
            mutate(newp[i])
        for i in range(POP):
            for j in range(N):
                p[i][j] = newp[i][j]
    best = 0
    for i in range(1, POP):
        if fitness(p[i]) < fitness(p[best]):
            best = i
    print("\nBest Schedule:", end=" ")
    for i in range(N):
        print("J" + str(p[best][i] + 1), end=" ")
    print("\nMinimum Waiting Time:", fitness(p[best]))
main()
