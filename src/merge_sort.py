from src.my_array import MyArray


def merge_sorted_arrays(left: MyArray, right: MyArray) -> MyArray:
    result = MyArray()

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(array: MyArray) -> MyArray:
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge_sorted_arrays(left_half, right_half)
