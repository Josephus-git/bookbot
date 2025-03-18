import sys

from stats import *



def main():
    try:
        name, book = sys.argv
        # book = "books/frankenstein.txt"
        file_cont = get_book_text(book)
        words_dict = words_with_count(file_cont)
        word_count = num_words(file_cont)

        # formating of word count
        print(f"{"="*10} BOOKBOT {"="*10} ")
        print(f"Analyzing book found at {book}...")
        print(f"{"-"*10} Word Count {"-"*10} ")
        print(f"Found {word_count} total words")
        print(f"{"-"*10} Character Count {"-"*10} ")
        
        for i in words_dict:
            print(f"{i}: {words_dict[i]}")
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    




main()
