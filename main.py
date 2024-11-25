FILENAME = "books/frankenstein.txt"

#create a main function to read the book
def main():
    #read the book
    with open(FILENAME) as f:
        file_contents = f.read()
    #print the book
    #print(file_contents)
    #print the word count of the book
    print(len(file_contents.split()))

#call the main function
if __name__ == "__main__":
    main()