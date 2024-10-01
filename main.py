def main():
    book_path = "books/frankenstein.txt"
    book_text = text_from_book(book_path)
    num_words = book_word_count(book_text)
    char_dict = character_occurences(book_text)
    removed_alpha = remove_non_alpha(char_dict)
    sorted_dict = sort_dict(removed_alpha)
    #print(sorted_dict)
    print_report(sorted_dict, num_words, book_path)

def text_from_book(book_path):
    with open(book_path) as f:
        book_as_text = f.read()
        return book_as_text

def book_word_count(book):
    book_list = book.split()
    return len(book_list)

def character_occurences(book):
    characters = {}
    for i in book:
        c = i.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def remove_non_alpha(dict):
    new_dict = {}
    for i in dict:
        if i.isalpha():
            new_dict[i] = dict[i]
    return new_dict

def sort_dict(dict):
    sorted_dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    return sorted_dict

def print_report(c_dict, words, title):
    print(f"Book summary for {title}")
    print(f"The book contains {words} words in total")
    print(f"Here's how often each character occur in the text:")
    for i in c_dict:
        k, v = i
        print(f"The character \"{k}\" shows up {v} times.")


main()