def decimal_to_binary(decimal_num):
    
    if decimal_num == 0:
        return "0"

    remainders = []
    org_num = decimal_num

    
    while decimal_num > 0:
        remainder = decimal_num % 2
        remainders.append(remainder)
        decimal_num //= 2  

    binary_str = ""
    for digit in reversed(remainders):
        binary_str += str(digit)

    return binary_str

number = float(input("Enter a decimal number: "))
if number < 0:
    print("Please enter a non-negative integer.")
else:
    binary_result = decimal_to_binary(number)
    print(f"The binary representation of {number} is {binary_result}")
