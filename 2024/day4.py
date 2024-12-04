input = []

with open("day4.txt", "r") as file:
    for line in file:
        input += [line.rstrip()]

needle = 'XMAS'
count = 0
needle_reversed = needle[::-1]


def check(word):
    return word == needle or word == needle_reversed


for i, row in enumerate(input):
    for j, _ in enumerate(row):
        if j + len(needle) <= len(row):
            if check(row[j:j+len(needle)]):
                count += 1

        if i + len(needle) <= len(input):
            word = ''.join(input[i+k][j] for k in range(len(needle)))
            if check(word):
                count += 1

        if i + len(needle) <= len(input) and j + len(needle) <= len(row):
            word = ''.join(input[i+k][j+k] for k in range(len(needle)))
            if check(word):
                count += 1

        if i + len(needle) <= len(input) and j - len(needle) >= -1:
            word = ''.join(input[i+k][j-k] for k in range(len(needle)))
            if check(word):
                count += 1

print('found:', count)
