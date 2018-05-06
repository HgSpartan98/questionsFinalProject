
    q = ""
    print()
    input_answer = (input(q).lower()).strip()
    answer = "" 
    if str(answer) in str(input_answer):
        print(yes.center(80, '-'))
    else:
        print(no.center(80, '-'))


        
    List  = [["question1", "answer1", ""], ["question2", "answer2"]]

    for q, a, graphic in List:
        userInput = input(q)
        print()
        print("The correct answer is", a)
