nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

res = map(lambda x, y : x + y, nums1, nums2)
print("Addition of two lists: ")
print(list(res))

nums = [1, 2, 3, 4, 5]
def sq(n):
    return n * n
square = list(map(sq, nums))
print("Square of numbers in a list:")
print(square)