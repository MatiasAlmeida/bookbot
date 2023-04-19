def words_count(book):
    count = len(book.split())
    return count

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    total_words = words_count(file_contents)
    print(f"There are {total_words} words in the book.")
