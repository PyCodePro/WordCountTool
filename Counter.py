import string

# Open the file for reading
filename = input("Enter the name of the file: ")
with open(filename, 'r') as file:
    # Read the contents of the file and convert to lowercase
    contents = file.read().lower()

    # Remove punctuation marks
    for char in string.punctuation:
        contents = contents.replace(char, '')

    # Split the contents into words and count the number of words
    words = contents.split()
    num_words = len(words)

    # Display the word count
    print("The file contains {} words.".format(num_words))
    
    #FOR MORE TUTORIALS/SCRIPTS PLEASE VISIT https://pycode.pro
