if __name__ == '__main__':
    with open('input2.txt', 'r') as f:
        lines = f.readlines()

    x = 0
    y = 0
    aim = 0

    for line in lines:
        direction, value = line.strip().split(' ')
        if direction == 'forward':
            x += int(value)
            y += int(value) * aim
        elif direction == 'down':
            aim += int(value)
        else:
            aim -= int(value)

    print(x * y)