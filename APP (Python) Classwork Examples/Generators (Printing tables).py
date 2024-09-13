def table_generator(number):
    for i in range(1, 11):
        yield i * number

input_number = 4
count = 1
table = table_generator(input_number)

for value in table:
    print(count, "X", input_number, "=", value)
