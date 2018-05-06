# Star Trek Memory test

def main():

    print("The following examination is designed to test the memory of a",
          "previously incapacitated individual. If you answer a question",
          "incorrectly, you will not be able to go back, but must proceed",
          "to the next question.")
    
    print()
    
    yes = 'CORRECT'
    no = 'INCORRECT'

    q1 = ("Where were the first conclusive advances made on toroidal"
    "space-time distortion and by whom? ")
    print()
    input_answer = (input(q1).lower()).strip()
    # we need to account for the fact that capitalization is not always consistent
    # and spaces are sometimes added
    answer = "cambridge" and "massachusetts" and "ralph seron"
    # answer must include the keywords: "Cambridge, Massachusetts, Ralph Seron"
    if str(answer) in str(input_answer):
        print(yes.center(80, '-'))
    else:
        print(no.center(80, '-'))
    
    q2 = ('Who said, "Logic is the cement of our civilization with which we'
    ' ascend from chaos using reason as our guide"? ')
    print()
    input_answer = input(q2).strip() # capitalization matters 
    answer = "T'Plana-Hath" and "matron of Vulcan Philosphy" 
    if str(answer) in str(input_answer):
        print(yes.center(80, '-'))
    else:
        print(no.center(80, '-'))
       
    q3 = ("What is the molecular formula of Yominum Sulfide crystals? ")
    print()
    input_answer = (input(q3)).strip() # capitalization matters
    answer = "K4Ym3(SO73Es2)" 
    if str(answer) in str(input_answer):
        print(yes.center(80, '-'))
    else:
        print(no.center(80, '-'))
          
    q4 = ('What significant contribution to bioengineering was made on the'
          'Loonkerian outpost on Klendth? ')
    print()
    input_answer = (input(q4).lower()).strip()
    answer = "universal atmospheric element compensator" 
    if str(answer) in str(input_answer):
        print(yes.center(80, '-'))
    else:
        print(no.center(80, '-'))

    q5 = ("Evaluate and conclude: A starship's sensors indicate it is being,",
    "pursued so closely that it occupies the same space as its pursuer.")
    print()
    input_answer = (input(q5).lower()).strip()
    answer = "warp drive regulators" and "parallax matter echo" 
    if str(answer) in str(input_answer):
        print(yes.center(80, '-'))
    else:
        print(no.center(80, '-'))
    # The warp drive regulators are creating a parallex matter echo.
          
    q6 = ('Identify the object and its cultural significance. ') #(include picture)
    print()
    input_answer = (input(q6).lower()).strip()
    answer = "Klingon mummification glyph" and "Zanxthkolt Dynasty" 
    if str(answer) in str(input_answer):
        print(yes.center(80, '-'))
    else:
        print(no.center(80, '-'))
          
    q7 = "What was Kiri-kin-tha's first law of metaphysics? "
    print()
    input_answer = (input(q7).lower()).strip()
    answer = "nothing unreal exists" 
    if str(answer) in str(input_answer):
        print(yes.center(80, '-'))
    else:
        print(no.center(80, '-'))
          
    q8 = "Adjust the sine wave of this magnetic envelope so that",
    "anti-neutrons can pass through it but anti-gravitons cannot. "
    a8 # user uses GUI to manipulate graph
          
    q10 = "How do you feel? "
    print()
    print("You have completed the examination.")

main()

          
    
          
