""" Define a class Countdown that takes a starting number and counts down to 0. Implement the
__iter__ and __next__ methods to make Countdown an iterator. Create an instance and use a
for-loop to iterate through the countdown sequence.
Concepts Covered: Iterators """

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration  
        else:
            current_value = self.current
            self.current -= 1 
            return current_value
          
countdown = Countdown(5)

for number in countdown:
    print(number)
