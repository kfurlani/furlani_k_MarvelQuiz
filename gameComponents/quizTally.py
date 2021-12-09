from gameComponents import vars


def total(value): 

    if value == 0:
        character = vars.character[1]

        print('\033[32m' + "Your tricks won't help you here " + character)

    if value == 500:
        character = vars.character[3]

        print('\033[34m' + "You're obviously " + character)

    if value == 700:
        character = vars.character[0]

        print('\033[31m' + "My spidey senses are tingling you must be " + character)
    
    if value == 800:
        character = vars.character[2]

        print('\033[35m' + "Not even the Time Stone can help you here " + character)
    
    if value >= 801: 
        character = vars.character[4]    

        print('\033[33m' + "I thought we got rid of you... " + character)

   
    


        
