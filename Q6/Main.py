from AI_Project.Q6.Genetics import Genetics
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

matrix = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         ]

matrix = matrix + np.transpose(matrix)

q1 = []
q2 = []


parameter = []
numberOfGenerations = [5, 50, 50]
populationSize = [10, 100, 10]
mutationRate = [0.01, 0.02, 0.05, 0.1]
tornumentSize = [10, 100, 10]

for gen in numberOfGenerations:
    for pop in populationSize:
        for mute in mutationRate:
            if pop == 10:
                        fig, ax = plt.subplots()
                        # ax.plot(a, c, 'k--', label='Model length')
                        # ax.plot(a, d, 'k:', label='Data length')
                        # ax.plot(a, c + d, 'k', label='Total message length')
                        g = Genetics(matrix, 4, gen, pop, 2, mute)
                        a, b, c = g.generation()
                        plt.plot(a, label="min")
                        plt.plot(b, label="average")
                        plt.plot(c, label="max")
                        plt.title("Gen:{} pop:{} mute:{} torn:{}".format(gen,pop,mute,2))
                        plt.xlabel("Number of Generation")
                        plt.ylabel("fitness")
                        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                        plt.show()


            else:
                for i in [2, 5, 10]:
                        g = Genetics(matrix, 4, gen, pop, i, mute)
                        a, b, c = g.generation()
                        plt.plot(a, label="min")
                        plt.plot(b, label="average")
                        plt.plot(c, label="max")
                        plt.title("Gen:{} pop:{} mute:{} torn:{}".format(gen, pop, mute, i))
                        plt.xlabel("Number of Generation")
                        plt.ylabel("fitness")

                        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
                        plt.show()


