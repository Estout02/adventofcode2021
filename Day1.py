def get_input(string):
    with open(string) as f:
        puzzle_input = f.readlines()
        return puzzle_input
def findIncreases(depths):
    ## start at 1 per instructions
    increases = 0
    past_depth = 0
    for d in depths:
        if past_depth == 0:
            past_depth = d
            increases += 1
        else:
            if d > past_depth:
                increases += 1
            past_depth = d
    return increases


def main():
    test_depths = get_input("input/test_d1_2")
    test_increases = findIncreases(test_depths)
    assert(test_increases == 10), "Does not equal 10"

    depths = get_input("input/day1")
    increases = findIncreases(depths)
    print(str(increases))





if __name__ == "__main__":
    main()