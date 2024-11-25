#set global variables for the book we are working with.
FILENAME = "books/frankenstein.txt"

def get_book_text(path):
    #get the text from the book
    with open(path, "r") as f:
        return f.read()

def count_words(text):
    #count the words in the text
    return len(text.split())

def main():
    #get the text from the book through a function
    text = get_book_text(FILENAME)
    #count the words in the text through a function
    num_words = count_words(text)
    #print the results
    print(f"There are {num_words} words in {FILENAME}")



#call the main function
if __name__ == "__main__":
    main()