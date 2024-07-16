# Your task is to calculate the number of trailing zeros in the factorial n!.
# For example, 20!=2432902008176640000 and it has 4 trailing zeros.
# Input
# The only input line has an integer n.
# Output
# Print the number of trailing zeros in n!.
# Constraints

# 1 \le n \le 10^9

# Example
# Input:
# 20

# Output:
# 4

n = int(input().strip())

def trailing_zeroes(n):
    if n == 0:
        return 0
    else:
        return n // 5 + trailing_zeroes(n // 5)
    
print(trailing_zeroes(n))



