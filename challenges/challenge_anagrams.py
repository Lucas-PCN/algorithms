def quick_sort(string):
    if not string:
        return []
    return (quick_sort([letter for letter in string[1:] if letter < string[0]])
            + [string[0]] +
            quick_sort([letter for letter in string[1:] if letter >= string[0]]))


def is_anagram(first_string, second_string):
    first_word = list(first_string.lower())
    second_word = list(second_string.lower())

    first_word_sorted = quick_sort(first_word)
    second_word_sorted = quick_sort(second_word)

    first = "".join(first_word_sorted)
    second = "".join(second_word_sorted)

    if not first_string or not second_string:
        return (first, second, False)
    if first_word_sorted != second_word_sorted:
        return (first, second, False)
    else:
        return (first, second, True)
