# join up smallest pairs
# take diff of each pair
# add all up distances

left, right = [], []

with open("day1.txt", "r") as file:
    for line in file:
        parts = line.rstrip().split(" ")
        a, b = int(parts[0]), int(parts[-1])
        left.append(a)
        right.append(b)

left.sort()
right.sort()

out = 0

while left and right:
    dist = abs(left.pop() - right.pop())
    out += dist

print(out)