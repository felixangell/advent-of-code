# very specific order
# X|Y means if both page x and page y are produced in an update
# X must be printed before Y.

# first, page order rules.

# which updates are already in the right order.

import collections


def correctify(rules, update, fix=False):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            rule = rules[update[j]]
            if update[i] in rule:
                if fix:
                    update[i], update[j] = update[j], update[i]
                    return correctify(rules, update, True)
                else:
                    return 0

    return int(update[len(update)//2])


with open("day5.txt", "r") as file:
    rules_for_page = collections.defaultdict(list)

    updates = []

    for line in file:
        line = line.rstrip()

        if '|' in line:
            parts = line.split('|')
            rules_for_page[int(parts[0])].append(int(parts[1]))
        elif line == '':
            continue
        else:
            # it's an update.
            updates += [[int(x) for x in line.split(',')]]

    p1, p2 = 0, 0
    for update in updates:
        p1 += correctify(rules_for_page, update, False)
        p2 += correctify(rules_for_page, update, True)

    print(p1, "...", (p2 - p1))
