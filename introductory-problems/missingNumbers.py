
# Input:

# 5
# 2 3 1 5
# Output:

# 4

n = int(input().strip())
arr = list(map(int, input().strip().split()))

myset = set(range(1, n + 1))
# 1 2 3 5

for ele in arr:
    myset.remove(ele)

print(myset.pop())
    