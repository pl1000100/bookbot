import sys

def main():
    book_path = "books/frankenstein.txt"
    file_content = get_file_content(book_path)
    words_count = get_num_words(file_content)
    chars_dict = get_num_of_every_char(file_content)
    chars_sorted_list = dict_to_sorted_list(chars_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in document")
    print()

    print("Characters in documents:")
    
    for i in chars_sorted_list:
        if i["name"].isalpha():
            print(f"Character {i["name"]} was found {i["val"]}")

    print("--- End report ---")

def dict_to_sorted_list(dict):
    li = []
    for i in dict:
        li.append({"name":i, "val":dict[i]})
    li.sort(reverse=True, key=sort_on)
    return li

def sort_on(dict):
    return dict["val"]

def get_num_of_every_char(text):
    chars = {}
    text_lowercase = text.lower()

    for char in text_lowercase:
        if char not in chars:
            chars[char] = 1
        else: 
            chars[char] += 1
    return chars

def get_num_words(text):
    return len(text.split())

def get_file_content(path_to_file):
    with open(path_to_file) as f:
        return f.read()

if __name__ == '__main__':
    sys.exit(main())
