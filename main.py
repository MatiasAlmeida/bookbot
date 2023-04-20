import os

def words_count(book):
    count = len(book.split())
    return count

def char_n_reps(book):
    book_words = book.split()
    char_dictionary = {}
    char_appearances = []
    for word in book_words:
        for ch in word:
            if ch.lower() not in char_appearances and ch.isalpha():
                char_appearances.append(ch.lower())
                char_dictionary[ch.lower()] = 1
            elif ch.isalpha():
                char_dictionary[ch.lower()] += 1
    return char_dictionary

def print_report(character_dictionary, filepath):
    character_list = []
    for ch in character_dictionary:
        character_list.append((ch, character_dictionary[ch]))
    character_list.sort()
    total_words = words_count(file_contents)
    print(f"--- Begin report of {filepath} ---")
    print(f"{total_words} found in the document")
    for ch in character_list:
        print(f"The '{ch[0]}' character was found {ch[1]} times")


with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    file_path = os.path.relpath(os.path.abspath(f.name), os.path.abspath("."))
    char_reps = char_n_reps(file_contents)
    # print(f"Character reps array: {char_reps}")
    print_report(char_reps, file_path)
