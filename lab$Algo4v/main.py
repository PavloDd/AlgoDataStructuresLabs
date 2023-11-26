from collections import deque


with open('input.txt', 'r') as file:
    lines = file.readlines()


matrix = []
for line in lines:
    row = list(map(int, line.strip().split()))
    matrix.append(row)


def find_zeros(matrix):
    zero_indices = set()

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_indices.add((i, j))

    return zero_indices

zero_indices = find_zeros(matrix)


def update_elements(matrix, zero_indices):
    rows = len(matrix)
    cols = len(matrix[0])

    def is_in_zero_indices(row, col):
        return (row, col) in zero_indices

    for i in range(rows):
        for j in range(cols):
            if is_in_zero_indices(i, j):
                for row_offset in range(-1, 2):
                    for col_offset in range(-1, 2):
                        new_row, new_col = i + row_offset, j + col_offset
                        if 0 <= new_row < rows and 0 <= new_col < cols and not is_in_zero_indices(new_row, new_col):
                            matrix[new_row][new_col] = 0

    return matrix


def shortest_path(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    graph = {}

    start_nodes = [(row, 0) for row in range(rows) if matrix[row][0] == 1]
    end_nodes = [(row, cols - 1) for row in range(rows) if matrix[row][cols-1] == 1]
    path_lengths = []

    for start_node in start_nodes:
        queue = deque([start_node])
        visited = set()
        distances = {start_node: 0}

    while queue:
        node = queue.popleft()
        visited.add(node)

        neighbors = []
        i, j = node
        for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = i + row_offset, j + col_offset
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] == 1:
                neighbors.append((new_row, new_col))

        graph[node] = neighbors

        for neighbor in neighbors:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                distances[neighbor] = distances[node] + 1

        if node in end_nodes:
            path_lengths.append(distances[node])

    return min(path_lengths) if path_lengths else -1


updated_matrix = update_elements(matrix, zero_indices)
shortest_path = shortest_path(updated_matrix)
print(shortest_path)


with open('output.txt', 'w') as file:
    file.write(str(shortest_path))
