import sys
from stats import count_words, count_characters, sort_char_count

def get_book_text(file_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        file_path (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(file_path) as file:
        return file.read()

def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    # Path to the book file
    book_file_path = sys.argv[1]
    print(f"Analyzing book found at {book_file_path}...")
    
    # Get the book text
    book_text = get_book_text(book_file_path)

    # Get the words count
    num_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Get the characters and sort
    char_count = count_characters(book_text)
    char_count_sorted = sort_char_count(char_count)

    print("--------- Character Count -------")
    for line in char_count_sorted:
        if line["char"].isalpha():
            print(f"{line["char"]}: {line["num"]}")
    print("============= END ===============")
main()