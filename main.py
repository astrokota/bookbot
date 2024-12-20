def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
 
    return word_count
    

def count_words(file_contents):

    if file_contents.strip() == "":
        return 0

    words = file_contents.split()

    return len(words)

    

main()

