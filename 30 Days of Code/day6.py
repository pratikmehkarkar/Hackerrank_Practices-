# Day-6 Python (Pratik Mehkarkar)
# Objective
# Today we will expand our knowledge of strings, combining it with what we have already learned about loops. Check out the Tutorial tab for learning materials and an instructional video.
# Task
# Given a string S of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).
# Note:  is considered to be an even index.
# Example
#
# Print abc def
# Input Format
# The first line contains an integer,  (the number of test cases).
# Each line  of the  subsequent lines contain a string, .
# Constraints
#
#
# Output Format
# For each String  print 's even-indexed characters, followed by a space, followed by 's odd-indexed characters.
# Sample Input
# 2
# Hacker
# Rank
# Sample Output
# Hce akr
# Rn ak
space = int(input())

for n in range(0, space):
    str1 = input()
    str1_length = len(str1)

    for i in range(0, str1_length):
        if i % 2 == 0:
            print(str1[i], end='')
    print(" ", end='')

    for j in range(0, str1_length):
        if j % 2 != 0:
            print(str1[j], end='')
    print(" ")
