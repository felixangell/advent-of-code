input = []

with open("day4-p2.txt", "r") as file:
    for line in file:
        input += [line.rstrip()]

needle = 'MAS'
count = 0
needle_reversed = needle[::-1]


def check(word):
    return word == needle or word == needle_reversed


count = 0

for i, row in enumerate(input):
    for j, _ in enumerate(row):
        if row[j] == 'A':
            first = []
            second = []

            if i - 1 >= 0 and j - 1 >= 0 and i + 1 < len(input) and j + 1 < len(row):
                first = [input[i - 1][j - 1], input[i][j], input[i + 1][j + 1]]

            if i - 1 >= 0 and j + 1 < len(row) and i + 1 < len(input) and j - 1 >= 0:
                second = [input[i - 1][j + 1],
                          input[i][j], input[i + 1][j - 1]]

            if first and second and check(''.join(first)) and check(''.join(second)):
                count += 1

print('found:', count)
