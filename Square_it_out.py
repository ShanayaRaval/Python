def find_squares(start, end):
    squares = [i*i for i in range(start, end+1)]

    even_squares = [x for x in squares if x % 2 == 0]
    odd_squares = [x for x in squares if x % 2 != 0]

    print("All squares:", squares)
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)

find_squares(1, 5)