# Final Project
# Aeowyn Kendall and Daniel Kim

# We need to build a program which will give the user a choice between two quizzes
# then call questions from a txt file, ask for user input, and check the input
# for certain keywords, and output different text if the keywords match

# This code fetches the indicated question

def question(qNumber, qSet):
    if readQ != True:
        qSet += ".txt"
        infile = open(qSet, "r")
        for i in range(qNumber):
            

        textQ = infile.readline()

        infile.closed

        global read
        readQ = True


