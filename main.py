def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    letter_tally = count_alpha_chars(book_text)
    gen_report(book_path, num_words, letter_tally)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    word_count = len(words)

def count_alpha_chars(str):
    tally = {}
    lowered_str = str.lower()
    for i in range (0, len(str)):
        curr_char = lowered_str[i]
        if curr_char.isalpha():
            if curr_char in tally:
                tally[curr_char]["count"] += 1 #(works with dictionary structure)
            else:
                tally[curr_char] = {
                    "letter" : curr_char,
                    "count" : 1
                }
                tally[curr_char]["count"] = 1
    return tally

def sort_on_num(dict):
    return dict["count"]

def gen_report(book_path, word_count, letter_tally ):

    list_tally = list(letter_tally.values())
    list_tally.sort(reverse=True, key=sort_on_num)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    print()
    for item in list_tally:
        l = item["letter"]
        c = item["count"]
        print(f"The '{l}' character was found {c} times")
    print("--- End report ---")

main()