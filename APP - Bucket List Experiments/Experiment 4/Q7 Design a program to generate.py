""" Design a program to generate all combinations of n pairs of balanced parentheses. """

def generate_parentheses(n):
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    result = []
    backtrack('', 0, 0)
    return result


n = 3 
combinations = generate_parentheses(n)
print("All combinations of ", str(n), " pairs of balanced parentheses:")
for combo in combinations:
    print(combo)
