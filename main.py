def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
  
    print(f"{word_count} words found in the document")

    print("")
    
    characters_dict = character_count(file_contents)

    for character in characters_dict:
        print(f"The '{character}' character was found {characters_dict[character]} times")

    print("--- End report ---")
    
def count_words(file_contents):

    return len(get_words(file_contents))

def character_count(file_contents):

    characters = {}
    words = get_words(file_contents)

    for word in words:
        for character in word:
            if character.isalpha():
                lower = character.lower()
                if lower in characters:
                    characters[lower] += 1
                else:
                    characters[lower] = 1

    return characters
   
def get_words(file_contents):

    if file_contents.strip() == "":
        return []

    return file_contents.split()

main()

