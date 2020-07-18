def bad_sort(list): # insertion sort
    for i in range(1, len(list)):
        current_item = list[i]
        j = i - 1
        while current_item < list[j] and j >= 0:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = current_item
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
    return good_sort(left) + [pivot] + good_sort(right)

array = [22, 55, 2, 88, 25, 35, 47, 30]
print(bad_sort(array))
print(good_sort(array))

