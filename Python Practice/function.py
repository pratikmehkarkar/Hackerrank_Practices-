def is_leap(year):
    # Write your logic here
    test_1 = year % 100
    test_2 = year % 400

    if test_2 == 0:
        return True
    if test_1 == 0:
        return False
    if year % 4 == 0:
        return True
    
    return False

year = int(input())
print(is_leap(year))