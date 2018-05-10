def analyzeAnswer():

    yes = "CORRECT"
    no = "INCORRECT"

    count = 0
    
    while True:
        
        try:
            count += 1
            q = dictionaryQ[count]
            input_answer = (input(q).lower()).strip()
            answer = dictionaryA[count]
            
            if str(answer) in str(input_answer):
                print(yes.center(80, '-'))
            else:
                print(no.center(80, '-'))
                
        except KeyError:
            break 
            
analyzeAnswer()
