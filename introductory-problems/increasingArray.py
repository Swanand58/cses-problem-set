# The first input line contains an integer n: the size of the array.
# Then, the second line contains n integers x_1,x_2,\ldots,x_n: the contents of the array.
# Output
# Print the minimum number of moves.
# Constraints

# 1 \le n \le 2 \cdot 10^5
# 1 \le x_i \le 10^9

# Example
# Input:
# 5
# 3 2 5 1 7

# Output:
# 5

n = int(input())
arr = list(map(int, input().split()))

total = 0
first = arr[0]

# for i in range(1, n):


