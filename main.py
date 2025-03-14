from sys import *
from stats import get_number_words, get_char_count,sort_char_count

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    content = get_book_text(argv[1])
    word_count = get_number_words(content)    
    print(f"Found {word_count} total words")
    char_count = get_char_count(content)
    sorted_char_count = sort_char_count(char_count)
    
    for char in sorted_char_count:
        print(f"{char['char']}: {char['count']}")

def get_book_text(path):
    
    with open(path, 'r') as f:
        return f.read()

main()