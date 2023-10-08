def can_fit_all(N, W, H, size):
    rows = size // W
    cols = size // H
    return rows * cols >= N


def min_square_size(N, W, H):
    left = 1
    right = max(W, H) * N

    while left < right:
        mid = (left + right) // 2
        if can_fit_all(N, W, H, mid):
            right = mid
        else:
            left = mid + 1

    return left


N, W, H = map(int, input().split())


print(min_square_size(N, W, H))


