# AOC Day 1
# Author: Umar Hassan
# 1 December


def part_one():
    cur_location = 50

    # read every line in the instructions
    with open("data/aoc-2025-day1.txt") as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:])

            if direction == "R":
                cur_location += distance
            else:
                cur_location -= distance

            print(cur_location)

    # if we've landed on 0, keep track of this


def part_two():
    pass


if __name__ == "__main__":
    part_one()
