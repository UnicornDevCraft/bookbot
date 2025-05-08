def count_words(book_text):
    """
    Counts the number of the words in a string and returns it.

    Args:
        book_text (str): The contents of the book.

    Returns:
        words_count (int): The number of words in the book.
    """
    words_count = len(book_text.split())
    return words_count
    

def count_characters(book_text):
    """
    Counts the number of times each character, (including symbols and spaces), appears in the string and returns it.

    Args:
        book_text (str): The contents of the book.

    Returns:
        char_count (dict): Each character and the number of times each character, (including symbols and spaces), appears in the string.
    """
    count = 1
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = count
    return char_count  

# A helper function that takes a dictionary and returns the value of the "num" key
def sort_on(dict):
    return dict["num"]


def sort_char_count(char_count):
    """
    Takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
    Args:
        char_count (dict): Each character and the number of times each character, (including symbols and spaces), appears in the string.
    Returns:
        char_count_sorted (list): Sorted list of dictionaries from greatest number of occurances to lowest.
    """
    char_count_sorted = []
    char_num = {}
    for char in char_count:
        char_num["char"] = char
        char_num["num"] = char_count[char]
        char_count_sorted.append(char_num)
        char_num = {}
    char_count_sorted.sort(reverse=True, key=sort_on)
    return char_count_sorted
