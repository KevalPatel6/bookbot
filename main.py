from stats import get_num_words, charcter_count, sorted_by_character_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    charc_dict = charcter_count(text)
    sorted = sorted_by_character_count(charc_dict)
    char_count_details = ""
    for char_val_pair in sorted:
        if char_val_pair["char"].isalpha():
            char_count_details += f"{char_val_pair["char"]}: {char_val_pair["count"]}\n"

    print(f"""
============ BOOKBOT ============\n
Analyzing book found at {path}...\n
----------- Word Count ----------\n
Found {num_words} total words\n
--------- Character Count -------\n
{char_count_details}
============= END ==============""")

main()

