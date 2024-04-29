def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    
    # print (file_contents)

    words = file_contents.split()
    word_count = len(words)
    letter_tally = count_alpha_chars(file_contents)
    gen_report(book_path, word_count, letter_tally)

def count_alpha_chars(str):
    tally = {}
    lowered_str = str.lower()
    #print(len(lowered_str))
    for i in range (0, len(str)):
    # for i in range (0, 100):
        curr_char = lowered_str[i]
        
        
        # print(type(curr_char))
        # print("----------")
        # print(f"curr char is {curr_char}")
        if curr_char.isalpha():
            # print(f"tally is {tally}")
            # print("---")
            ##### works
            # if curr_char in tally:
            #     tally[curr_char]["count"] += 1 #(works with dictionary structure)
            #     # tally[curr_char] += 1
            # else:
            #     if curr_char.isalpha():
            #         tally[curr_char] = {"count" : 1} #works (returns dictionary)
            #         # tally[curr_char] = 1
            
            ###testing different dictionary structure
            if curr_char in tally:
                # print(f"{curr_char} exists in tally")
                # print(f"tally[{curr_char}] is {tally[curr_char]}")
                tally[curr_char]["count"] += 1 #(works with dictionary structure)
                # print(f"new tally[{curr_char}] is {tally[curr_char]}")
                # tally[curr_char] += 1
            else:
                # print(f"{curr_char} not in tally")
                tally[curr_char] = {
                    "letter" : curr_char,
                    "count" : 1
                }
                # tally[curr_char] = {"count" : 1} #works, but weird structure: new is tally is {'letter': 'p', 'p': {'count': 1}}
                tally[curr_char]["count"] = 1
                # print(f"new is tally is {tally}")
                # tally[curr_char] = 1
        #else:
            # print("curr_char fails .isalpha()")
    #     print("---")
    # print(tally)
    
    return tally

def sort_on_num(dict):
    return dict["count"]

def gen_report(book_path, word_count, letter_tally ):

    # list_tally = list([letter_tally.keys()][letter_tally.items()]) #doesn't work
    list_tally = list(letter_tally.values())
    # print(letter_tally)
    # print(list_tally)
    list_tally.sort(reverse=True, key=sort_on_num)
    # print("------")
    # print(list_tally)
    

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    print()
    for item in list_tally:
        l = item["letter"]
        c = item["count"]
        print(f"The '{l}' character was found {c} times")
        # print(f"item is {item}")
    print("--- End report ---")

main()