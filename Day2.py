import Day1


def parseDirections(list):
    horizontal_pos = 0
    depth = 0
    for l in list:
        if l.startswith("forward"):
            l.split(" ", 1)
            horizontal_pos += int(l[-2])
        elif l.startswith("down"):
            l.split(" ", 1)
            depth += int(l[-2])
        elif l.startswith("up"):
            l.split(" ", 1)
            depth -= int(l[-2])
        else:
            break
    return horizontal_pos * depth

def parseDirectionsRound2(list):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for l in list:
        if l.startswith("forward"):
            l.split(" ", 1)
            numb = l[-2]
            horizontal_pos += int(l[-2])
            depth += aim * int(l[-2])
        elif l.startswith("down"):
            l.split(" ", 1)
            aim += int(l[-2])
        elif l.startswith("up"):
            l.split(" ", 1)
            aim -= int(l[-2])
        else:
            break
    return horizontal_pos * depth

def main():
    trajectory = Day1.get_input("input/day2.txt")
    product = parseDirections(trajectory)
    print(product)

    trajectory2 = Day1.get_input("input/day2.txt")
    product2 = parseDirectionsRound2(trajectory2)
    print(product2)


if __name__ == "__main__":
    main()