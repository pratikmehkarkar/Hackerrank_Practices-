# Day-9 (Pratik Mehkarkar)
import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    return 1 if n == 1 else factorial(n - 1) * n
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()