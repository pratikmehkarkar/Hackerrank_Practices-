# Day - 6 (Pratik Mehkarkar)
# Objective
# In this challenge, we will use loops to do some math. Check out the Tutorial tab to learn more.
# Task
# Given an integer, n, print its first 10 multiples. Each multiple n*i should be printed on a new line in the form: n x i = result.
# Sample Input
# 2
# Sample Output
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20

import math
import os
import random
import re
import sys

n = int(input())
for i in range(1,11):
    print(n,"x",i,"=",n*i)
