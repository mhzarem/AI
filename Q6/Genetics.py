import numpy as np
from statistics import *


class Genetics:

    def __repr__(self):
        return "input matrix \r\n {}" \
               "\r\n generation: \r\n{}".format(np.matrix(self.input_matrix), [x for x in self.init_generation()])

    def __init__(self, input_matrix, color_number, number_of_generation, population_size, tornument_size, mutation_rate):
        self.input_matrix = input_matrix
        self.number_of_generation = number_of_generation
        self.population_size = population_size
        self.tornument_size = tornument_size
        self.mutation_rate = mutation_rate
        self.color_number = color_number
        self.population = self.init_generation()

    def init_generation(self):
        population = []
        size = len(self.input_matrix)
        for i in range(0, self.population_size):
            population.append([np.random.randint(1, self.color_number) for _ in range(0, size)])
        return population

    def evaluation(self, instance):
        cost = 0
        size = len(self.input_matrix)
        m = int((np.count_nonzero(np.matrix(self.input_matrix))) / 2)
        # print(m)
        for i in range(0, size):
            for j in range(0, size):
                if self.input_matrix[i][j] == 1:
                    if instance[i] != instance[j]:
                        cost = cost + 1
        return cost / (2 * m)

    def sel_parents(self, k):
        result = []
        for _ in range(0, self.tornument_size):
            parents = []
            for _ in range(0, k):
                test = self.population[np.random.randint(0, len(self.population))]
                parents.append([test, self.evaluation(test)])
                
            parents = sorted(parents, key=lambda item: item[0], reverse=True)
            # print(parents)
            result.append(parents[0][0])
        # print(result)
        return result

    def cross_over(self):
        parents = self.sel_parents(4)
        childs = []
        # print(parents)
        for i in range(0, self.tornument_size):
            for j in range(0, i):
                size = len(self.input_matrix)
                split_point = np.random.randint(0, len(self.input_matrix))
                # print(split_point)
                a, b = [], []
                for pilot in range(0, split_point):
                    a.append(parents[i][pilot])
                    b.append(parents[j][pilot])

                for pilot in range(split_point, size):
                    a.append(parents[j][pilot])
                    b.append(parents[i][pilot])

                childs.append(a)
                childs.append(b)
        # print(childs)
        return childs

    def mutation(self):
        size = len(self.input_matrix)
        num = int(size * self.population_size * self.mutation_rate)
        for _ in range(0, num):
            self.population[np.random.randint(0, len(self.population))][np.random.randint(0, size)] = np.random.randint(0,self.color_number)

    def generation(self):
        max_gen_list = []
        min_gen_list = []
        avr_gen_list = []
        re_ev = []
        for _ in range(0, self.number_of_generation):
            self.population = self.cross_over()
            self.mutation()
            for item in self.population:
                re_ev.append(self.evaluation(item))
            max_gen = max(re_ev)
            min_gen = min(re_ev)
            avr_gen = mean(re_ev)
            max_gen_list.append(max_gen)
            min_gen_list.append(min_gen)
            avr_gen_list.append(avr_gen)

        return min_gen_list, avr_gen_list, max_gen_list



