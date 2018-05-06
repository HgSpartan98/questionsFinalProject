# Final Project
# Aeowyn Kendall and Daniel Kim

# We need to build a program which will give the user a choice between two quizzes
# then call questions from a txt file, ask for user input, and check the input
# for certain keywords, and output different text if the keywords match

# This code fetches the indicated question


def main():
    compileQuestions("testQuestions")
    print(questionList)

def compileQuestions(qSet):
    count = 0
    currentLine = "Stuff"
    global questionList
    questionList = {}
    qSet += ".txt"
    infile = open(qSet, "r")
    while True:
        count += 1
        currentLine = infile.readline().strip()
        if currentLine == "end":
            break
        questionList[count] = currentLine

    infile.close()
