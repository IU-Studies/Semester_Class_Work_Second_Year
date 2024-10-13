""" Create a generator function count_up_to that counts from 1 to a given number. Maintain internal
state in the generator to keep track of the current number. Use this generator to count up to 7 and
print the numbers.
Concepts Covered: Generators with State """

def count_up_to(max_num):
    current = 1  
    while current <= max_num:
        yield current
        current += 1  
      
for number in count_up_to(7):
    print(number)
