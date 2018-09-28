x = 1
while True:
    y = x * 7
    if y % 6 == 5:
        if y % 5 == 4:
            if y % 4 == 3:
                if y % 3 == 2:
                    if y % 2 == 1:
                        print(y)
                        break
    x += 1

x = 1
while True:
    y = x * 7
    if y % 6 == 5 and y % 5 == 4 and y % 4 == 3 and y % 3 == 2 and y % 2 == 1:
        print(y)
        break
    x += 1

x, y, z = 6, 5, 4
if x < y:
    small = x
    if z < small:
        small = z
elif y < z:
    small = y
else:
    small = z