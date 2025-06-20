def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(book_content):
    words = book_content.split()
    return len(words)

def get_character_count(book_content):
    characters = list(book_content)
    character_count = {}

    for character in characters:
        ch = character.lower()
        character_count[ch] = character_count.get(ch, 0) + 1

    return character_count

def sort_on(items):
    return items["num"]

def get_ch_count_list(ch_count_dict):
    records = []

    for k, v in ch_count_dict.items():
        char_dict = {}
        char_dict["char"] = k
        char_dict["num"] = v

        records.append(char_dict)

    records.sort(reverse=True, key=sort_on)

    return records

