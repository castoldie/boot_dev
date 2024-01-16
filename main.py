'''
main file
'''

def main():
    '''
    docstring
    '''
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_num_words(text):
    '''
    docstring
    '''
    words = text.split()
    return len(words)

def sort_on(_d):
    '''
    docstring
    '''
    return _d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    '''
    docstring
    '''
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_chars_dict(text):
    '''
    docstring
    '''
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    '''
    docstring
    '''
    with open(path, mode='r', encoding="utf-8") as file:
        return file.read()

main()
