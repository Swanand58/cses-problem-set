# You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
# Input
# The only input line contains a string of n characters.
# Output
# Print one integer: the length of the longest repetition.
# Constraints

# 1 \le n \le 10^6

# Example
# Input:
# ATTCGGGA

# Output:
# 3

line = input()

line = line.upper()

count = 1
maxCount = 1

for i in range(len(line) - 1):
    if line[i] == line[i+1]:
        count += 1
    else:
        if count > maxCount:
            maxCount = count
        count = 1

if count > maxCount:
    maxCount = count

print(maxCount)