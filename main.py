import random
import hangman_art
import hangman_word_list_of_animals as hgwl 
import rules
random_letter = random.choice(hgwl.word_list) 
# print(random_letter)
lives = 6
correct_letter = []
game_over = False

hangman_art.welcome()
print(rules.rule)
print(f"This word contains {len(random_letter)} letters")
while not game_over:

    print(hangman_art.stages[-lives-1])
    print(f"Total no of lives remaining: {lives}")
    
    user_input = input("Guess a letter: ").lower()
    
    if user_input in display:
        print(f"Please enter another letter {user_input} already exist")              
    
     
    display = ""

    
    for letter in random_letter:
        if letter == user_input:
            # print("Right")
            display += letter
            correct_letter.append(letter)
            # display -= "_"
        elif letter in correct_letter:
            display += letter    
            
  
        else:
            # print("Wrong")  
               
            display += "_"

    if not user_input in display:
        lives-=1

    if not "_" in display:
        game_over = True
        hangman_art.won()
    if lives == 0:
        game_over = True
        print(hangman_art.stages[-1]) 
        hangman_art.lose()
        print("Game over hangman died")   


    print(display)
