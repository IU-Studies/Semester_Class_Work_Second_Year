""" Implement a program to solve the fractional knapsack problem where you can take fractions of items. """

def fractional_knapsack(capacity, values, weights):
    value_weight_ratios = []
    for i in range(len(values)):
        value_weight_ratios.append((values[i] / weights[i], values[i], weights[i]))

    value_weight_ratios.sort(reverse=True, key=lambda x: x[0])

    total_value = 0  
    for ratio, value, weight in value_weight_ratios:
        if capacity == 0:
            break
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            capacity = 0  

    return total_value

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value = fractional_knapsack(capacity, values, weights)
print("Maximum value in the knapsack:", max_value)
