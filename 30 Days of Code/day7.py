# Day-7 (Pratik Mehkarkar)
# Objective
# Today, we will learn about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video.
# Task
# Given an array,A , of N integers, print A's elements in reverse order as a single line of space-separated numbers.
# Example
# A = [1,2,3,4]
# Print 4 3 2 1. Each integer is separated by one space.
# Input Format
# The first line contains an integer,  (the size of our array).
# The second line contains  space-separated integers that describe array 's elements.
if __name__ == '__main__':
    n = int(input())

    arr = str(input()).split(" ")
    arr.reverse()
    for num in arr:
        print(num + " ", end="")