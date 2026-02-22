#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    for i in my_list:
        if i not in unique:
            unique.append(i)
    total = 0
    for i in unique:
        total += i
    return total
