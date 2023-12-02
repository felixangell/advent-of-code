def parse_sg(sg):
    return [p.strip().split(' ') for p in sg]

Red = 12
Green = 13
Blue = 14

impossible = set()
possible = set()

# Game <num>: cubes; cubes; cubes
def calc(line: str) -> int:
    parts = line.split(':')
    game = parts[0]

    cubes = ''.join(parts[1:]).strip().split(';')
    sub_games = [parse_sg(c.split(',')) for c in cubes]

    for sg in sub_games:
        cubes = [(int(c[0]), c[1]) for c in sg]
        for cube in cubes:
            if cube[1] == 'red' and cube[0] > Red:
                impossible.add(game)
            elif cube[1] == 'green' and cube[0] > Green:
                impossible.add(game)
            elif cube[1] == 'blue' and cube[0] > Blue:
                impossible.add(game)
            else:
                possible.add(game)


with open("day2.txt", "r") as file:
    for line in file:
        calc(line)

    print(impossible)
    print(sum([int(i.split(' ')[1]) for i in possible]))
    # print(x)