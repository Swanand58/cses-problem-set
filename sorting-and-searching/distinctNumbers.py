# You are given a list of n integers, and your task is to calculate the number of distinct values in the list.
# Input
# The first input line has an integer n: the number of values.
# The second line has n integers x_1,x_2,\dots,x_n.
# Output
# Print one integers: the number of distinct values.

# Constraints

# 1 <= n <= 2 . 10^5
# 1 <= x_i <= 10^9

# Example
# Input:
# 5
# 2 3 2 2 3

# Output:
# 2

n = int(input())
arr = list(map(int, input().split()))

if n == 0:
    print(0)

arr.sort()
count = 1

for i in range(1, n):
    if arr[i] != arr[i-1]:
        count += 1

print(count)