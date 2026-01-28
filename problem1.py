# Sum of distinct elements
set1 = [3, 1, 7, 9]
set2 = [2, 4, 1, 9, 3]

total = 0

# Check each element in the first set
for num in set1:
    if num not in set2:
        total += num

# Check each element in the second set 
for num in set2:
    if num not in set1:
        total += num

print("Sum of distinct elements:", total)