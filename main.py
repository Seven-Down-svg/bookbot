#set global variables for the book we are working with.
FILENAME = "books/frankenstein.txt"

def get_book_text(path):
    #get the text from the book
    with open(path, "r") as f:
        return f.read()

def count_words(text):
    #count the words in the text
    return len(text.split())


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


#creat function to take the char_dict from the character_count function and sort it. 
def unsort_dict(dict):
    #set the empty list to append too. 
    result = []
    #use a for loop to loop through each item in the dict
    for char, count in dict.items():
        #append the mini dictionary to the list. 
        result.append({"char": char, "num": count})
    return result


#used for the .sort to sort for the most numerous characters in the book. 
def sort_key(dict):
    return dict["num"]

def main():
    #get the text from the book through a function
    text = get_book_text(FILENAME)
    #count the words in the text through a function
    num_words = count_words(text)
    #count of each character
    count_char = character_count(text)
    #unsort the count_char dictionary
    unsorted_count_char = unsort_dict(count_char)
    #sort unsorted dict. 
    unsorted_count_char.sort(reverse=True, key=sort_key)
    #print the results
    print(f"There are {num_words} words in {FILENAME}")
    #print an format the dictionary that contains all char counts. 
    for num in range(len(unsorted_count_char)):
        print(f"The {unsorted_count_char[num]['char']} was found {unsorted_count_char[num]['num']} times")
    
    #print end report.
    print("--- End of Report ---")
        


#call the main function
if __name__ == "__main__":
    main()
