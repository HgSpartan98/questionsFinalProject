# Final Project
# Aeowyn Kendall and Daniel Kim

# We need to build a program which will give the user a choice between two quizzes
# then call questions from a txt file, ask for user input, and check the input
# for certain keywords, and output different text if the keywords match

# This code fetches the indicated question
# Call compileToDictionary with the name of the file with the appended file type
# in a string. It will return a dictionary with each line of the file assigned
# a number equivalent to its line in the file

def main():
    questionList = compileToDictionary("testQuestions.txt")
    
    print(questionList)

def compileToDictionary(fileName):
    count = 0
    currentLine = "Stuff"
    dictionary = {}
    infile = open(fileName, "r")
    while True:
        count += 1
        currentLine = infile.readline().strip()
        if currentLine == "":
            break
        dictionary[count] = currentLine

    infile.close()
    return dictionary
