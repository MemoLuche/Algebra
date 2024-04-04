def difference_max_min(list_nums):
    max_num = 1
    min_num = 1
    for i in list_nums:
        if i > max_num:
            max_num = i
            continue
        elif i < min_num:
            min_num = i
            continue
        else:
            continue
    difference = max_num - min_num
    return difference

def max_num(list_nums):
    max_num = 0
    min_num = 0
    for i in list_nums:
        if i > max_num:
            max_num = i
            continue
        elif i < min_num:
            min_num = i
            continue
        else:
            continue
    return max_num

def min_num(list_nums):
    max_num = 0
    min_num = 0
    for i in list_nums:
        if i > max_num:
            max_num = i
            continue
        elif i < min_num:
            min_num = i
            continue
        else:
            continue
    return min_num

# take integer inputs and convert it to list
numbers = list(map(int, input().split()))

# call the function
print(max_num(numbers))
print(min_num(numbers))
print(difference_max_min(numbers))