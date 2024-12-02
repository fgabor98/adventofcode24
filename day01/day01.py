#!/usr/bin/python3

from typing import TextIO

def calc_dist_and_sim(f: TextIO) -> int:

    left_col = []
    right_col = []

    for line in f:
        nums = line.strip().split()
        left_col.append(int(nums[0]))
        right_col.append(int(nums[1]))

    sim = 0
    for i in range(len(left_col)):
        sim += right_col.count(left_col[i]) * left_col[i]

    left_col.sort()
    right_col.sort()

    dist = 0
    for i in range(len(left_col)):
        dist += abs(left_col[i] - right_col[i])

    return dist, sim


if __name__ == "__main__":

    try:
        with open("../input/input01.txt", "r") as f:
            dist, sim = calc_dist_and_sim(f)
        print(dist, sim)
    except Exception as e:
        print(f"An error of type {type(e).__name__} occurred: {e}")
