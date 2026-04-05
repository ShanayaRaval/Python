L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original list: ", L)

count = 0

for i in L:
    count += i

avg = count / len(L)

print("Sum is: ", count)
print("Average is: ", avg)

L.sort()

print("Smallest element is: ", L[0])

print("Greatest element is: ", L[-1])