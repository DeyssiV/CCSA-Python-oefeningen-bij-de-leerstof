def bubble_sort(a):
    counter = 0
    for i in range(0, len(a) - 1, 1):
        for j in range (len(a)-1, i, -1):
            counter = counter+1
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
        print(a)
    print (f"Voor een rij van lengte {len(a)} werd het if-statement {counter} keer uitgevoerd")
    return a
if __name__ == "__main__":
    a = [int(_) for _ in input().split()]
    bubble_sort(a)