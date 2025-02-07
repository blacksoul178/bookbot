def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = get_num_count(text)
    print(f"words in text: {wordcount}")
    get_character_count(text)
    
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
        
def get_num_count(text):
    words = text.split()
    return len(words)

def get_character_count(book_text):
    character_count = {"Character":"value"}
    lower_case_text= book_text.lower()
    for character in lower_case_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    
    for character in character_count:
        if character.isalpha():
            print(f"The '{character}' character was found {character_count[character]} times")




main()