""" Define a generator function square_numbers that yields the squares of numbers from 1 to 5. Iterate
through the generator to print each squared number.
Concepts Covered: Generators """

def square_numbers():
    for i in range(1, 6):
        yield i * i  

for square in square_numbers():
    print(square)
