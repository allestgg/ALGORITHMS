# This algorithm searches for an item in a list by checking each element in the list one by one.

def sequential_search(my_list, item):
    for i in range(len(my_list)):
        if my_list[i] == item:
            return True
    return False

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sequential_search(list1, 5))  # True
print(sequential_search(list1, 11))  # False