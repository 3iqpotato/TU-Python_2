import random
import scipy.io
import matplotlib as plt
import numpy as np

classroom_width = 7
classroom_lenght = 5
num_app = 5
population_size = 12
generations = 10
mutation_rate = 0.1


def calculate_signal_strenght(ap_x, ap_y, point_x, point_y):
    distance = np.sqrt((ap_x - point_x) ** 2 + (ap_y - point_y) ** 2)
    return 1 / (distance + 1)


def visualize_initial_and_final(classroom_width, classroom_lenght, initial_population, final_population):
    plt.figure(figsize=(15, 6))

    for i, (x, y) in enumerate(initial_population):
        plt.text(x, y, str(i + 1), color='black', fontsize=8, ha='center', va='center')
    plt.scatter(*zip(*final_population), color='red', marker='o', label='start position of wifi points')

    for i, (x, y) in enumerate(initial_population):
        plt.text(x, y, str(i + 1), color='black', fontsize=8, ha='center', va='center')
    plt.scatter(*zip(*final_population), color='blue', marker='o', label='final position of wifi points')

    plt.xlabel('Ширина на учебната зала (м)')
    plt.ylabel('Дължина на учебната зала (м)')
    plt.title('Начално и карайно разпределение на точките за достъп')
    plt.legend()
    plt.show()


def visualize_dynamic_changes(classroom_width, clasroom_lenght, population, fitness_scores):
    for generation in range(generations):
        plt.figure(figsize=(15, 6))
        plt.subplot(1, 2, 1)
        ap_placements = population[generation]
        x = np.linspace(0, classroom_width, 100)
        y = np.linspace(0, clasroom_lenght, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.zeros_like(X)
        for ap_x, ap_y in ap_placements:
            Z += calculate_signal_strenght(ap_x, ap_y, X, Y)
        plt.pcolormesh(X, Y, Z, shading='auto', cmap='viridis')
        plt.color(lebel='Сила на сигнала')
        for i, (x, y) in enumerate(ap_placements):
            plt.text(x, y, str(i + 1), color='black', fontsize=8, ha='center', va='center')
        plt.scatter(*zip(*ap_placements), color='red', marker='o', label='distribution of points')
        plt.xlabel('Ширина на учебната зала (м)')
        plt.ylabel('Дължина на учебната зала (м)')
        plt.title(f'сила на wi-fi сигнала и разпределение на точките за достъп(Поколение {generation + 1})')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(range(1, generation + 2), fitness_scores[:generation + 1], marker='o')
        plt.xlabel('поколение')
        plt.ylabel('резултати')
        plt.title('резултати от фитнеса за различните поколения')

        plt.tight_layout()
        plt.show

        initial_population = [(random.uniform(0, classroom_width), random.uniform(0, classroom_lenght)) for _ in
                              range(population_size)]
        population = [initial_population.copy()]

        best_solution = None
        best_fitness = float('-inf')
        all_fitness_scores = []

        for generations in range(generations):
            fitness_scores = []
            for ap_x, ap_y in population[generations]:
                coverage = 0
                for point_x in range(classroom_width):
                    for point_y in range(clasroom_lenght):
                        coverage += calculate_signal_strenght(ap_x, ap_y, point_x, point_y)
                    fitness_scores.append(coverage)
    if max(fitness_scores) > best_fitness:
        best_solution = population[generation][fitness_scores.index(max(fitness_scores))]
        best_fitness = max(fitness_scores)
    all_fitness_scores.append(max(fitness_scores))
    selected_parents = random.choices(population[generations], weights=fitness_scores, k=population_size)
    offspring = []
    for _ in range(population_size):
        parent1, parent2 = random.simple(selected_parents, 2)
        crossover_x = random.uniform(parent1[0], parent2[0])
        crossover_y = random.uniform(parent1[1], parent2[1])
        offspring.append((crossover_x, crossover_y))
    for i in range(len(offspring)):
        if random.random() < mutation_rate:
            offspring[i] = (random.uniform(0, classroom_width), random.uniform(0, clasroom_lenght))
    population.append(offspring)
    visualize_initial_and_final(classroom_width, classroom_lenght, initial_population, population[-1])
    visualize_dynamic_changes(classroom_width, clasroom_lenght, population, all_fitness_scores)
    trajectory_scores = []
    for generations in range(generation + 1):
        distances = [np.linalg.norm(np.array(point) - np.array(best_solution)) for point in population[generations]]
        trajectory_scores.append(np.mean(distances))
    plt(figsize=(10, 6))
    plt(range(generations + 1), trajectory_scores, marker='o')
    plt.xlabel('genetation')
    plt.ylabel('Medium distance the best solution')
    plt.title('trajectory of population')
    plt.show()

    plt.figure()
    plt.plot(range(1, generations + 1), all_fitness_scores, marker='o')
    plt.xlabel('genetation')
    plt.ylabel(' Best fitness result')
    plt.title('graphic of similaryity')
    plt.show()