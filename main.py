#set global variables for the book we are working with.
FILENAME = "books/frankenstein.txt"

def get_book_text(path):
    #get the text from the book
    with open(path, "r") as f:
        return f.read()

def count_words(text):
    #count the words in the text
    return len(text.split())

#STILL NEED TO TEST
def character_count(text):
    #set the initial dictionary for the alphabet
    char_dict = {}
    #iterate through each character in the text
    for char in text:
        #lowercase the char
        char = char.lower()
        #check if the char is alpha and add to the dictionary. 
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    #return the dictionary. 
    return char_dict

def main():
    #get the text from the book through a function
    text = get_book_text(FILENAME)
    #count the words in the text through a function
    num_words = count_words(text)
    #count of each character
    count_char = character_count(text)
    #print the results
    print(f"There are {num_words} words in {FILENAME}")
    #print the dictionary that contains all char counts. 
    print(count_char)


#call the main function
if __name__ == "__main__":
    main()
