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
# N, C = map(int, input().split())
# free_sections = list(map(int, input().split()))

# Виводимо отримані значення для перевірки
# print("N:", N)
# print("W:", C)
# print("Free sections:", free_sections)


# def find_minimum_distance_between_agro_cows(N, C, free_sections):
#
#     distances = [C + 1]
#     all_possible_distances = []
#     free_sections.sort(reverse=True)
#     if N >= C:
#         for i in range(len(free_sections) - 1):
#             for j in range(i+1, len(free_sections)):
#                 distance = free_sections[i] - free_sections[j]
#                 if free_sections[i-1]-free_sections[j-1] > distance > free_sections[i+1] - free_sections[j+1]:
#                     all_possible_distances.append(distance)
#     else:
#         print("Wrong data")
#     print(all_possible_distances)
#
#     all_possible_distances.sort(reverse=True)
#     distances = all_possible_distances[:C + 1]
#     print(min(distances))
#     print(distances)
#     #task isn`t completed because i have some problems with logic
#
#
# find_minimum_distance_between_agro_cows(N, C, free_sections)

def can_place_cows(sections, distance, c):
    cows_placed = 1
    last_cow_position = sections[0]
    occupied_sections = [sections[0]]
    for i in range(1, len(sections)):
        if sections[i] - last_cow_position >= distance:
            cows_placed += 1
            last_cow_position = sections[i]
            occupied_sections.append(sections[i])
            if cows_placed == c:
                return True, occupied_sections
    return False, occupied_sections

def largest_min_distance(N, C, free_sections):
    free_sections.sort()
    left = 1
    right = free_sections[-1] - free_sections[0] + 1
    result = 0
    occupied_sections = []
    while left <= right:
        mid = (left + right) // 2
        can_place, occupied_sections = can_place_cows(free_sections, mid, C)
        if can_place:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result, occupied_sections


N = 5
C = 3
free_sections = [1, 2, 3, 4, 5, 10, 30, 40, 60, 90]
result, occupied_sections = largest_min_distance(N, C, free_sections)

print(result)
print(occupied_sections)




