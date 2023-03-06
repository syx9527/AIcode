import random

population_size = 100


# Define a gene
class Gene:
    def __init__(self):
        self.genes = []
        for i in range(0, 8):
            bit = random.randint(0, 1)
            self.genes.append(bit)

    def __str__(self):
        return ''.join(str(x) for x in self.genes)

    # Define a population


class Population:
    def __init__(self):
        self.population = []
        for i in range(0, population_size):
            gene = Gene()
            self.population.append(gene)

        # Define a fitness function


def fitness_function(gene):
    return gene.genes.count(1)


# Selection
def selection():
    sorted_population = sorted(population.population,
                               key=fitness_function, reverse=True)
    return sorted_population[:int(0.2 * population_size)]


# Crossover
def crossover(parent1, parent2):
    child = Gene()
    for i in range(len(parent1.genes)):
        if parent1.genes[i] != parent2.genes[i]:
            # randomly choose from parent genes
            if parent1.genes[i] > parent2.genes[i]:
                bit = random.randint(parent2.genes[i], parent1.genes[i])
            else:
                bit = random.randint(parent1.genes[i], parent2.genes[i])
            child.genes[i] = bit
        else:
            # copy the gene from parent
            child.genes[i] = parent1.genes[i]
    return child


# Mutation
def mutate(gene):
    for i in range(len(gene.genes)):
        bit = random.randint(0, 1)
        gene.genes[i] = bit
    return gene


# Main loop
def main():
    global population
    population = Population()

    generation = 0

    while (fitness_function(population.population[0])
           != len(population.population[0].genes)):
        print('Generation : {}'.format(generation))
        # Selection
        parents = selection()

        # Crossover
        children = []
        print(len(parents))
        for i in range(0, int(0.2 * population_size), 2):


            parent1 = parents[i]
            parent2 = parents[i + 1]

            child = crossover(parent1, parent2)
            children.append(child)

            # Mutation
        for i in range(len(children)):
            children[i] = mutate(children[i])

        population.population = parents + children

        generation += 1

    print('Generation : {}'.format(generation))
    print('Best gene is {}'.format(population.population[0]))


if __name__ == '__main__':
    main()
