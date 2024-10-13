""" Create a class Fibonacci that generates the Fibonacci sequence up to a specified number of
elements. Implement the __iter__ and __next__ methods to make Fibonacci an iterator. Print the first
10 numbers in the Fibonacci sequence.
Concepts Covered: Custom Iterable, Iterators """

class Fibonacci:
    def __init__(self, num_elements):
        self.num_elements = num_elements
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.num_elements:
            raise StopIteration

        fib_value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return fib_value

fibonacci = Fibonacci(10)

for number in fibonacci:
    print(number)
