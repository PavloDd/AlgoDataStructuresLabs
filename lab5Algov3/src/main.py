class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, source, destination):
        self.add_node(source)
        self.add_node(destination)
        self.graph[source].append(destination)

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {', '.join(self.graph[node])}")


def read_input(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Розбиваємо рядки та витягуємо дані
    cities = lines[0].strip().split(',')
    storage = lines[1].strip().split(',')

    # Витягуємо газопроводи
    pipelines = [line.strip().split(',') for line in lines[2:]]

    return cities, storage, pipelines

# Задані міста, газосховища та газопроводи
# cities = ['Львів', 'Долина', 'Івано-Франківськ', 'Тернопіль', 'Чернівці', 'Луцьк', 'Рівне']
# storage = ['Сховище_1', 'Сховище_2', 'Сховище_3']
# pipelines = [['Сховище_1', 'Львів'], ['Сховище_1', 'Сховище_2'], ['Сховище_2', 'Долина'],
#               ['Львів', 'Сховище_3'], ['Сховище_3', 'Івано-Франківськ'], ['Чернівці', 'Рівне'],
#              ['Івано-Франківськ', 'Чернівці'], ['Івано-Франківськ', 'Тернопіль'], ['Луцьк', 'Чернівці'],
#              ['Луцьк', 'Тернопіль'], ['Долина', 'Львів'], ['Тернопіль', 'Долина']]


cities, storage, pipelines = read_input("./src/input.txt")

# Створення графу
gas_network = Graph()

# Додавання міст та газосховищ у граф
for city in cities + storage:
    gas_network.add_node(city)

# Додавання газопроводів у граф
for pipeline in pipelines:
    gas_network.add_edge(pipeline[0], pipeline[1])

# Виведення графу
gas_network.print_graph()

from collections import deque


def bfs_gas_supply(graph, storage):
    result = []

    for s in storage:
        visited = set()
        queue = deque([(s, [])])  # Початок з s
        current_result = set()

        while queue:
            current, path = queue.popleft()

            if current in visited:
                continue

            visited.add(current)

            if current not in storage:
                current_result.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited and neighbor not in storage:
                    queue.append((neighbor, path + [current]))

        not_reached_cities = set(graph.keys()) - visited - set(storage) - {s}
        not_reached_cities_list = list(not_reached_cities)

        result.append([s, not_reached_cities_list])

    return result


result = bfs_gas_supply(gas_network.graph, storage)


with open("./src/output.txt", 'w', encoding='utf-8') as file:
    for r in result:
        file.write(','.join(map(str, r)) + '\n')