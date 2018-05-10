def analyzeAnswer(dictionaryA, answerGiven, numberQ):


    answerReal = dictionaryA[numberQ]
    
    if str(answerReal) in str(answerGiven):
        return "CORRECT"
    else:
        return "INCORRECT"
