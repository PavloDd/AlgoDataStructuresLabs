def build_suffix_arr(needle):
    suffixes = [(needle[i:], i) for i in range(len(needle))]
    suffixes.sort(key=lambda x: x[0])
    return [s[1] for s in suffixes]


def automat(haystack, needle):
    suffix_array = build_suffix_arr(needle)

    m, n = len(haystack), len(needle)
    result = []

    for i in range(m):
        lp = 0
        j = suffix_array[0]

        while j < n and i + lp < m and needle[j] == haystack[i + lp]:
            lp += 1
            j += 1

        if lp == n:
            result.append(i)

    return result


haystack = "abcsdjaabab ababaabc"
needle = "abc"
result = automat(haystack, needle)
print(f"Індекси входжень: {result}")
