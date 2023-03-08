import os
import string 


# Get the current working directory
cwd = os.getcwd()

# Join the current working directory with the filename
filename = os.path.join(cwd, "file.txt")

# Open the file
with open(filename, "r") as file:
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
