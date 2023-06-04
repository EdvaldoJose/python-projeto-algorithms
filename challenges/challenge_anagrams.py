def is_anagram(first_string, second_string):
    if len(first_string) == 0 and len(second_string) == 0:
        return ('', '', False)

    sorted_string1 = ''.join(sorted_chars(first_string.lower()))
    sorted_string2 = ''.join(sorted_chars(second_string.lower()))

    is_anagram = sorted_string1 == sorted_string2

    return sorted_string1, sorted_string2, is_anagram


def sorted_chars(string):
    chars = list(string)

    quicksort(chars, 0, len(chars) - 1)

    return ''.join(chars)


def quicksort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1
