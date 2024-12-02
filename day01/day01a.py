#!/usr/bin/python3

from typing import TextIO

def calc_dist(f: TextIO) -> int:

    left_col = []
    right_col = []

    for line in f:
        nums = line.strip().split()
        left_col.append(int(nums[0]))
        right_col.append(int(nums[1]))
        sum += abs(left_col[i] - right_col[i])

    left_col.sort()
    right_col.sort()

    dist = 0
    for i in range(len(left_col)):
        dist += abs(left_col[i] - right_col[i])

    return dist


if __name__ == "__main__":

    try:
        with open("../sample/sample01.txt", "r") as f:
            dist = calc_dist(f)
        print(dist)
    except Exception as e:
        print(f"An error of type {type(e).__name__} occurred: {e}")
