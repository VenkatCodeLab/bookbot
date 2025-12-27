import sys
from stats import get_words_num, count_characters, chars_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]
    book = get_book_text(bookpath)
    wordcount=get_words_num(book)
    print(f"Found {wordcount} total words")
    charcount=count_characters(book)
    chars_sorted_list = chars_dict_to_sorted_list(charcount)
    print_report(bookpath, wordcount, chars_sorted_list)


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()

    
