def is_palindrome_recursive(word, low_index, high_index):

    if len(word) == 0:
        return False
    if low_index >= high_index:
        return True

    first_char = word[low_index]
    last_char = word[high_index]

    if first_char != last_char:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
