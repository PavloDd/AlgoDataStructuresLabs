# import heapq
#
#
# def a_star(graph, start, goal):
#     queue = [(0, start)]
#     visited = set()
#
#     while queue:
#         cost, node = heapq.heappop(queue)
#
#         if node in visited:
#             continue
#
#         visited.add(node)
#
#         if node == goal:
#             return True
#
#         for neighbor, weight in graph[node]:
#             if neighbor not in visited:
#                 heapq.heappush(queue, (cost + weight, neighbor))
#
#     return False
#
#
# def find_unreachable_gas_stations(cities, gas_stations, pipelines):
#     graph = {}
#
#     # Build the graph
#     for pipeline in pipelines:
#         station_from, station_to = pipeline
#         for station in [station_from, station_to]:
#             if station not in graph:
#                 graph[station] = []
#
#     for pipeline in pipelines:
#         station_from, station_to = pipeline
#         graph[station_from].append((station_to, 1))  # Assuming all pipelines have the same weight
#
#     result = []
#
#     # Check reachability for each gas station and city
#     for station in gas_stations:
#         unreachable_cities = []
#         for city in cities:
#             if not a_star(graph, station, city):
#                 unreachable_cities.append(city)
#         result.append([station, unreachable_cities])
#
#     return result
#
#
# # Example usage:
# cities = ['Lviv', 'Stryi', 'Dolyna']
# gas_stations = ['Storage_1', 'Storage_2']
# pipelines = [['Lviv', 'Stryi'], ['Dolyna', 'Lviv'], ['Storage_1', 'Storage_2']]
#
# unreachable_results = find_unreachable_gas_stations(cities, gas_stations, pipelines)
# print(unreachable_results)

import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost

def astar(start, goal):
    heap = [(0, start)]
    visited = set()

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        if current_node == goal:
            return current_cost

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, cost in current_node.neighbors.items():
            heapq.heappush(heap, (current_cost + cost, neighbor))

    return float('inf')

def find_unreachable_cities(storage, cities, pipelines):
    unreachable_cities = {}

    for storage_name in storage:
        storage_node = Node(storage_name)

        for pipeline in pipelines:
            source, destination = pipeline
            if source == storage_name:
                storage_node.add_neighbor(destination, 1)

        for city in cities:
            if city != storage_name:
                city_node = Node(city)
                cost = astar(storage_node, city_node)
                if cost == float('inf'):
                    if storage_name not in unreachable_cities:
                        unreachable_cities[storage_name] = []
                    unreachable_cities[storage_name].append(city)

    return unreachable_cities

# Приклад використання:

cities = ['Львів', 'Стрий', 'Долина', 'Мукачево']
storage = ['Сховище_1', 'Сховище_2']
pipelines = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Сховище_2']]

unreachable_cities = find_unreachable_cities(storage, cities, pipelines)

for storage_name, cities_list in unreachable_cities.items():
    print(f"Газосховище {storage_name}: {cities_list}")
