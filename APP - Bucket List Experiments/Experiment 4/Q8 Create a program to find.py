""" Create a program to find the minimum number of jumps needed to reach the end of an array,
where each element represents the maximum jump length at that position. """

def min_jumps(arr):
    if len(arr) <= 1:
        return 0  

    jumps = 0  
    current_end = 0  
    farthest = 0  

    for i in range(len(arr) - 1):  
        farthest = max(farthest, i + arr[i])

        if i == current_end:
            jumps += 1 
            current_end = farthest  

            if current_end >= len(arr) - 1:
                break

    return jumps
  
arr = [2, 3, 1, 1, 4]  
result = min_jumps(arr)
print("Minimum number of jumps to reach the end of the array: ", str(result))
