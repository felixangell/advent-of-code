def calc(line: str) -> int:
    nums = []
    for c in line:
        if c.isdigit():
            nums.append(c)
    if len(nums) == 1:
        return int(nums[0] + nums[0])
    return int(nums[0] + nums[len(nums) - 1])

with open("day1.txt", "r") as file:
    s = 0

    # TODO part 2.
    for line in file:
        s = s + calc(line)

    print(s)