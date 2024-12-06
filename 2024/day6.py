def is_out_of_bounds(x, y, width, height):
    return x < 0 or x >= width or y < 0 or y >= height

with open("day6.txt", "r") as file:
    w, h = -1, -1
    
    start = (0, 0)
    obstacles = {}
    direction = '^'
    choices = ['^', '>', 'v', '<']

    y = 0
    for line in file:
        line = line.rstrip()
        w = len(line)
        x = 0
        for ch in line:
            if ch == '#':
                obstacles[x + y * w] = True
            elif ch in choices:
                direction = ch
                start = (x, y)
            x += 1
        y += 1

    h = y

    pos = start
    
    def move(x, y, dir):
        if dir == '^':
            return x, y - 1
        if dir == 'v':
            return x, y + 1
        if dir == '>':
            return x + 1, y
        if dir == '<':
            return x - 1, y

    seen = set()

    def rotate(direction):
        index = choices.index(direction)
        return choices[(index + 1) % len(choices)]

    while True: # pos in bounds of map
        seen.add(pos)
        
        dx, dy = 0, 0

        if direction == '^':
            dx, dy = 0, -1
        if direction == '>':
            dx, dy = 1, 0
        if direction == '<':
            dx, dy = -1, 0
        if direction == 'v':
            dx, dy = 0, 1
        
        nxt = ((pos[0] + dx), (pos[1] + dy))
        
        if is_out_of_bounds(nxt[0], nxt[1], w, h):
            break

        if (nxt[0] + nxt[1] * w) in obstacles:
            # rotate direction 90 degrees.
            direction = rotate(direction)
            print(direction)

        nx, ny = move(pos[0], pos[1], direction)

        pos = (nx, ny)

    print(len(seen))

    # part 2.

    # 1. detect a cycle in a path
    # 2. if i put an obstacle at position X in the path, will i detect a cycle?