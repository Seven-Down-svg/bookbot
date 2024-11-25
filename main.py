
#create a main function to read the book
def main():
    #read the book
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print the book
    print(file_contents)

#call the main function
if __name__ == "__main__":
    main()