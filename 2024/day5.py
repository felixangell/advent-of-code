# very specific order
# X|Y means if both page x and page y are produced in an update
# X must be printed before Y.

# first, page order rules.

# which updates are already in the right order.

import collections

def is_correct(rules, update):
    # if contains both numbers
    # must have key before value.

    # val mapped to index
    # for each page in array
    # is idx of val > idx of other?

    # 75, 47, 61, 53, 29
    # 0   1   2   3   4

    # 75|47.
    # page 75 must be before 47.
    
    update_idx = {}
    for i, u in enumerate(update):
        update_idx[u] = i
    
    print(update_idx)

    for page in update:
        rfp = rules[page]
        for other in rfp:            
            if other in update_idx and (update_idx[other] < update_idx[page]):
                return False

    return True

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

    count = 0
    for update in updates:
        if is_correct(rules_for_page, update):
            print(update, "OK!")
            count += update[len(update)//2]

    print("count:", count)
