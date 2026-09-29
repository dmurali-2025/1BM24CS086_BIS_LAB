#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 5
#define POP 10
#define GEN 50

int burst[N] = {6, 2, 8, 3, 4};

int fitness(int s[])
{
    int wait = 0, time = 0;

    for (int i = 0; i < N; i++) {
        wait += time;
        time += burst[s[i]];
    }

    return wait;
}

void shuffle(int s[])
{
    for (int i = N - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        int t = s[i];
        s[i] = s[j];
        s[j] = t;
    }
}

void mutate(int s[])
{
    if (rand() % 10 == 0) {
        int i = rand() % N;
        int j = rand() % N;

        int t = s[i];
        s[i] = s[j];
        s[j] = t;
    }
}

int main()
{
    srand(time(NULL));

    int p[POP][N], newp[POP][N];

    // Initial population
    for (int i = 0; i < POP; i++) {
        for (int j = 0; j < N; j++)
            p[i][j] = j;
        shuffle(p[i]);
    }

    // Genetic Algorithm
    for (int g = 0; g < GEN; g++) {

        int best = 0;

        for (int i = 1; i < POP; i++)
            if (fitness(p[i]) < fitness(p[best]))
                best = i;

        printf("Generation %d: Waiting Time = %d\n",
               g + 1, fitness(p[best]));

        // Elitism: keep best solution
        for (int j = 0; j < N; j++)
            newp[0][j] = p[best][j];

        // Create remaining population
        for (int i = 1; i < POP; i++) {

            int a = rand() % POP;
            int b = rand() % POP;

            int parent = fitness(p[a]) < fitness(p[b]) ? a : b;

            // Copy parent
            for (int j = 0; j < N; j++)
                newp[i][j] = p[parent][j];

            // Simple mutation
            mutate(newp[i]);
        }

        // Replace population
        for (int i = 0; i < POP; i++)
            for (int j = 0; j < N; j++)
                p[i][j] = newp[i][j];
    }

    // Find final best solution
    int best = 0;

    for (int i = 1; i < POP; i++)
        if (fitness(p[i]) < fitness(p[best]))
            best = i;

    printf("\nBest Schedule: ");

    for (int i = 0; i < N; i++)
        printf("J%d ", p[best][i] + 1);

    printf("\nMinimum Waiting Time: %d\n", fitness(p[best]));

    return 0;
}