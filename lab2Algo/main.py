import unittest


def calculate_paint_time(malears_count, paint_time_per_meter, billboard_lengths):
    max_billboard_length = max(billboard_lengths)
    if malears_count >= len(billboard_lengths):
        return max_billboard_length * paint_time_per_meter
    else:
        billboards_per_malear = len(billboard_lengths) // malears_count
        meters_for_each_malear = []

        for i in range(0, len(billboard_lengths), billboards_per_malear):
            billboards_for_one_malear = billboard_lengths[i:i + billboards_per_malear]
            print(billboards_for_one_malear)
            meters_per_one_malear = sum(billboards_for_one_malear)
            meters_for_each_malear.append(meters_per_one_malear)
        return max(meters_for_each_malear) * paint_time_per_meter


class TestPaintBillboards(unittest.TestCase):
    def test_paint_time(self):
        self.assertEqual(calculate_paint_time(10, 5, [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]), 100)


def main():
    malears_count = int(input("Введіть кількість малярів: "))
    paint_time_per_meter = float(input("Введіть час фарбування одного метра (у годинах): "))
    billboard_lengths = list(map(int, input("Введіть довжину кожного щита через пробіл: ").split()))

    result = calculate_paint_time(malears_count, paint_time_per_meter, billboard_lengths)
    print(f"Загальний час фарбування щитів: {result} годин")


if __name__ == "__main__":
    main()
