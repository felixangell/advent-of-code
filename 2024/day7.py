# each line is an equation
# test value before each line.
# can numbers combined make test val?
# left to right. not precedence.
# add, multiply.

# sum of test values which are correct

from collections import deque


def calc(res, vals):
    q = deque([vals[0], ])        

    for num in vals[1:]:
        nq = deque()
        while q:
            cr = q.popleft()
            nq.append((cr + num))
            nq.append((cr * num))
            nq.append((int(str(cr) + str(num))))
        q = nq
    
    print(set(q))
    return res if res in set(q) else 0

with open("day7.txt") as file:
    count = 0
    
    for line in file:
        line = line.rstrip()
        
        val, opts = line.split(':')
        values = opts.strip().split(' ')

        count += calc(int(val), [int(v) for v in values])

    print("p1:", count)