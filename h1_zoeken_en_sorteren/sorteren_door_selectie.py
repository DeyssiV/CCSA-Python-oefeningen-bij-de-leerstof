def selection_sort_vooraan(a):
    for i in range(0,len(a) - 1, 1):
        positie = i
        min = a[i]
        for j in range(i+1, len(a), 1):
            if a[j] < min:
                positie = j
                min = a[j]

        a[positie] = a[i]
        a[i] = min
        print(a)
    return a

if __name__ == "__main__":
    a = [int(_) for _ in input().split()]
    selection_sort_vooraan(a)

