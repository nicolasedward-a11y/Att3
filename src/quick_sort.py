from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    if len(array) <= 1:
        return array

    pivot = array[len(array) - 1]

    left = MyArray()
    equal = MyArray()
    right = MyArray()

    for i in range(len(array)):
        if array[i] < pivot:
            left.append(array[i])

        elif array[i] > pivot:
            right.append(array[i])

        else:
            equal.append(array[i])

    left = quick_sort(left)
    right = quick_sort(right)

    result = MyArray()

    for i in range(len(left)):
        result.append(left[i])

    for i in range(len(equal)):
        result.append(equal[i])

    for i in range(len(right)):
        result.append(right[i])

    return result
