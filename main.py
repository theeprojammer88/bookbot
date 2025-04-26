from stats import count_words
from stats import count_chars
from stats import char_sort
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    num_words = count_words(file_contents)
    char_count = count_chars(file_contents)
    sorted_characters = char_sort(char_count)
    print("============ BOOKBOT ============")
    print(f"\nAnalyzing the book found at {file_path}...")
    print("\n----------- Word Count -----------")
    print(num_words)
    print("\n----------- Character Count -----------")

    for i in sorted_characters:
        print(f"{i["char"]}: {i["num"]}")

main()