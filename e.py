for n in range(100, 999 + 1):
    if int(str(n)[0]) ** 3 + int(str(n)[1]) ** 3 + int(str(n)[2]) ** 3 == n:
        print(n)

for r in range(4):
    for y in range(4):
        for g in range(7):
            if r + y + g == 8:
                print(r, y, g)
