# def can_fit_all(N, W, H, size):
#     rows = size // W
#     cols = size // H
#     return rows * cols >= N
#
#
# def min_square_size(N, W, H):
#     left = 1
#     right = max(W, H) * N
#
#     while left < right:
#         mid = (left + right) // 2
#         if can_fit_all(N, W, H, mid):
#             right = mid
#         else:
#             left = mid + 1
#
#     return left
#
#
# N, W, H = map(int, input().split())
#
#
# print(min_square_size(N, W, H)) #print

# Зчитуємо два інтових значення та масив
N, C = map(int, input().split())
free_sections = list(map(int, input().split()))

# Виводимо отримані значення для перевірки
print("N:", N)
print("W:", C)
print("Free sections:", free_sections)


def find_minimum_distance_between_agro_cows(N, C, free_sections):

    distances = [C + 1]
    all_possible_distances = []
    free_sections.sort(reverse=True)
    if N >= C:
        for i in range(len(free_sections) - 1):
            for j in range(i+1, len(free_sections)):
                distance = free_sections[i] - free_sections[j]
                all_possible_distances.append(distance)
    else:
        print("Wrong data")

    all_possible_distances.sort(reverse=True)
    distances = all_possible_distances[:C + 1]
    print(min(distances))
    print(distances)
    #task isn`t completed because i have some problems with logic


find_minimum_distance_between_agro_cows(N, C, free_sections)


