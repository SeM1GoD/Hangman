# |Imports|
import random


# |Functions|

def choose_word(file_path):

    ### 
    # Choosing A Random Word From Words File 
    # Output : |str| word_list - Returning The Choosen Word 
    ###

    with open(file_path, 'r') as words_file:
        words_list = []
        for line in words_file:
            words_list += [line.split("\n").pop(0)]
        words_file.seek(0)
        index = random.randint(0, len(words_list) - 1)
        return words_list[index]

def check_valid_input(letter_guessed, old_letter_guessed):

    ### 
    # Checking If Entered Letter Is Correct And Didn't Appears In Previous Guesses
    # Output : |bool| True - If The Letter Can Be Guessed
    # Output : |bool| False - If The Letter Can Not Be Guessed 
    ###

    letter_guessed = letter_guessed.lower()
    old_letter_guessed.sort()
    if (not(letter_guessed.isalpha()) or (len(letter_guessed) > 1)):
        print ("Do You Even Know How This Game Works? You Little Bitch")
        return False
    elif ((letter_guessed in old_letter_guessed)):
        print("Please Remember The Letters That You Already Tried To Guess And Dont Be Stupid!!!")
        print(" , ".join(old_letter_guessed))
        return False
    else:
        return True

def show_hidden_word(secret_word, old_letters_guessed): 

    ###  
    # Showing The Correct Guessed Letter In The Right Place Of The Word 
    # Output : |str| Hidden_word - String Of The Correct Guessed Letters In The Right Place
    ###
    hidden_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter + " "
        else:
            hidden_word += "_ "
    return hidden_word


def check_win(secret_word, old_letters_guessed): 

    ### 
    # cheking if all the letter guessed and the player wins 
    # Output : |bool| True - If The Player Succeeded To Guess The Word
    # Output : |bool| False - If The Player Do Not Succeeded To Guess The Word
    ###

    correct_letter_count = 0
    for letter in secret_word:
        if(letter in old_letters_guessed):
            correct_letter_count += 1
        else:
            continue
    if(correct_letter_count == len(secret_word)):
        return True 
    else:
        return False 

def print_hangman(num_of_tries):

    ###
    # Printing The Imgae Of Tries
    ###

    hangman_pic = {
"1": """    
    x-------x
""", 
"2": """    
    x-------x   
    |  
    | 
    |
    |   
    |  
""",  
"3": """    
    x-------x  
    |       | 
    |       0
    |   
    |  
    | 
""", 
"4": """    
    x-------x 
    |       |
    |       0   
    |       |  
    | 
    |
""",
"5": """    
    x-------x
    |       |   
    |       0  
    |      /|\\   
    |  
    | 
""", 
"6": """    
    x-------x 
    |       |
    |       0   
    |      /|\\
    |      /
    |   
""",   
"7": """    
    x-------x   
    |       |  
    |       0 
    |      /|\\  
    |      / \\   
    |  
"""}
    print(hangman_pic.get(str(num_of_tries)))
    
def welcome_massage(): 

    ###
    #Welcome To The Game Massage
    ###
    HANGMAN_ASCII_ART = """ 
    
Welcome To The Game: Hangmam


  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ 



"""
    
    print (HANGMAN_ASCII_ART)
    print("You Have 7 Tries. \nLets Check If You Are The King Of The Word \nOr You Are Gonna Kill Yourself")


# |Main Fanction|

def main (first_start_of_game):
    
    # Defining Variables
    file_path = r"words.txt"
    old_letters_guessed = []
    tries = 0


    # First Entering To The Game 
    if(first_start_of_game):
        welcome_massage()
        first_start_of_game = False
    
    # Main Menu
    start_game = input("""


1: Start New Game
2: Exit
    
Please Enter Your Choice: """)


    # Code
    if (start_game == "1"):
        secret_word = choose_word(file_path).lower()
        print(show_hidden_word(secret_word, old_letters_guessed))
        while tries < 8:
            letter_guessed = input ("Please Guess A Letter: ")
            if(not(check_valid_input(letter_guessed, old_letters_guessed))):
                continue
            old_letters_guessed += letter_guessed
            if(not(letter_guessed in secret_word)):
                tries += 1
                print_hangman(tries)
                print(tries)
                print(show_hidden_word(secret_word, old_letters_guessed))
                if(tries == 7):
                    print("\n\nYou Are So Dumb! If Your Grandpa Could, He Probebly Would Revive And Kill Himself")
                    break
                continue
            print(show_hidden_word(secret_word, old_letters_guessed))
            if(check_win(secret_word, old_letters_guessed)):
                print("\n\nEasy Peasy Lemon Squeezy")
                break
            else:
                continue
        main(False)
    elif (start_game == "2"):
        print("\n\nI Wish Someone Gonna Rape You. Dont Come Back You Fuckturd\n\n")
    else:
        print("\n\nOMG! Are You Testing My Code? Dont Be Such A Fool. Please. Just Follow The Rules And Have Fun")
        main(False)


if __name__ == "__main__":
    main(True)

        
            









