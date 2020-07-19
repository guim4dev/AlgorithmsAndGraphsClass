def bad_sort(list): # insertion sort
    for i in range(1, len(list)):
        current_item = list[i]
        j = i - 1
        while current_item < list[j] and j >= 0:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = current_item
        print(list)
    return list

def good_sort(list): # quick sort
    if len(list) <= 1:
        return list

    pivot_index = len(list)//2
    pivot = list[pivot_index]
    del list[pivot_index]

    left = []
    right = []

    for item in list:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)
    print(left + [pivot] + right)
    return good_sort(left) + [pivot] + good_sort(right)

array_bad = [2, 7, 5, 6, 9, 0, 1, 4, 8, 5, 3]
array_good = [2, 7, 5, 6, 9, 0, 1, 4, 8, 5, 3]
print("Bad Sort")
print(bad_sort(array_bad))
### Bad Sort Output
# [2, 7, 5, 6, 9, 0, 1, 4, 8, 5, 3]
# [2, 7, 5, 6, 9, 0, 1, 4, 8, 5, 3]
# [2, 5, 7, 6, 9, 0, 1, 4, 8, 5, 3]
# [2, 5, 6, 7, 9, 0, 1, 4, 8, 5, 3]
# [2, 5, 6, 7, 9, 0, 1, 4, 8, 5, 3]
# [0, 2, 5, 6, 7, 9, 1, 4, 8, 5, 3]
# [0, 1, 2, 5, 6, 7, 9, 4, 8, 5, 3]
# [0, 1, 2, 4, 5, 6, 7, 9, 8, 5, 3]
# [0, 1, 2, 4, 5, 6, 7, 8, 9, 5, 3]
# [0, 1, 2, 4, 5, 5, 6, 7, 8, 9, 3]
# [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
print("Good Sort")
print(good_sort(array_good))
### Good Sort Output
# [0, 2, 7, 5, 6, 9, 1, 4, 8, 5, 3]
# [1, 2, 7, 5, 6, 9, 4, 8, 5, 3]
# [2, 7, 5, 6, 4, 8, 5, 3, 9]
# [2, 3, 4, 7, 5, 6, 8, 5]
# [2, 3]
# [5, 5, 6, 7, 8]
# [5, 5]
# [7, 8]
# [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
