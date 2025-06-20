from stats import get_book_text, get_num_words, get_character_count, get_ch_count_list

def main():
    print("============ BOOKBOT ============")
    book_path = "./books/frankenstein.txt"

    content = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}")

    print("----------- Word Count ----------")
    num_words = get_num_words(content)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_count_list = get_ch_count_list(get_character_count(content))

    for item in char_count_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

main()
