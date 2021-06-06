# Day-8 (Pratik Mehkarkar)
# Objective
# Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure. Check out the Tutorial tab for learning materials and an instructional video!
# Task
# Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found, print Not found instead.
# Note: Your phone book should be a Dictionary/Map/HashMap data structure.
# Sample Input
# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry
# Sample Output
# sam=99912222
# Not found
# harry=12299933
# --------------------Solution------------------
n = int(input())
phone_directory = {}

for i in range(0, n):
    str1 = str(input()).split(" ")
    name = str1[0]
    phone = int(str1[1])
    phone_directory[name] = phone

while True:
    try:
        name = str(input())
        if name in phone_directory:
            phone = phone_directory[name]
            print(name + "=" + str(phone))
        else:
            print("Not found")
    except:
        break
