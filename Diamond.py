rs = int(input("Enter the number of rows:"))
if rs%2 == 0:
    halfdiamrow = int(rs/2)
else:
    halfdiamrow = int(rs/2) + 1
space = halfdiamrow - 1

for i in range (1, halfdiamrow + 1):
    for j in range (1, space +1):
        print(end = " ")

    space = space - 1
    num = 1
    for j in range (2 * i + 1)
    print(end = str(num))

