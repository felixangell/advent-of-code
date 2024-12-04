from collections import Counter

left, right = [], []

with open("day1.txt", "r") as file:
    for line in file:
        parts = line.rstrip().split(" ")
        a, b = int(parts[0]), int(parts[-1])
        left.append(a)
        right.append(b)

count = Counter(right)
similarity = 0

for num in left:
    if num in count:
        print(num, 'and', count[num])
        similarity += num * count[num]

left.sort()
right.sort()

res = 0

while left and right:
    dist = abs(left.pop() - right.pop())
    res += dist

print(similarity)
print(res)
