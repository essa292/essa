def square_it_out(start, end):
    squares = []
    for num in range(start, end + 1):
        squares.append(num ** 2)
    squares.sort()
    print(squares)

# Example usage
square_it_out(1, 10)
