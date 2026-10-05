def selection_sort_vooraan(a):
    for i in range(len(a) - 1, 0, -1):
        positie = i
        max = a[i]
        for j in range(i-1, -1, -1):
            if a[j] < max:
                positie = j
                max = a[j]

        a[positie] = a[i]
        a[i] = max
    return a

if __name__ == "__main__":
    a = [int(_) for _ in input().split()]
    print(selection_sort_vooraan(a))

