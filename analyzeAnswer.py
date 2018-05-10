def analyzeAnswer(dictionaryA, answerGiven, numberQ):


    answerReal = dictionaryA[numberQ]

    
    answers = dictionaryA[numberQ].split("$")

    if answers[0] == " ":
        return True
    elif len(answers) == 1:
        
        if str(answerReal) in str(answerGiven):
            return True
        else:
            return False
        
    elif len(answers) == 2:
        answerReal = answers[0] or answers[1]
        
        if str(answerReal) in str(answerGiven):
            return True
        else:
            return False
                
    elif len(answers) == 3:
        answerReal = answers[0] or answers[1] or answers[2]
        
        if str(answerReal) in str(answerGiven):
            return True
        else:
            return False
        

