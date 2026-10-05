def zoek_binair(zoekItem,rij):
    l = 0
    r = len(rij) - 1
    m = (l+r)//2

    while(l!=r):
        print(f"{l}, {r}")
        if (rij[m] < zoekItem):
            l = m + 1
        else :
            r = m
        m = (l+r)//2
        
    if (rij[m]==zoekItem):
        return rij.index(zoekItem)
    else:
        return -1

index = zoek_binair(70, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f"index = {index}")