# Зчитуємо два інтових значення та масив
N, W = map(int, input().split())
free_sections = list(map(int, input().split()))

# Виводимо отримані значення для перевірки
print("N:", N)
print("W:", W)
print("Free sections:", free_sections)



def find_minimum_distance_between_agro_cows(N, C, free_sections):

    distances = [C]
    all_possible_distances = []
    sorted_free_sections = free_sections.sort(reverse=True)
    if N >= C:
        for i in sorted_free_sections:
            for j in sorted_free_sections:
                distance = sorted_free_sections[i] - sorted_free_sections[j]
                all_possible_distances = []
                all_possible_distances.insert(distance)
    else:
        print("Wrong data")

    all_possible_distances.sort(reverse=True)
    distances = all_possible_distances[:C]
    return min(distances)

