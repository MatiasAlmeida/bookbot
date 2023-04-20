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

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    # total_words = words_count(file_contents)
    char_reps = char_n_reps(file_contents)
    print(f"Character reps array: {char_reps}")
