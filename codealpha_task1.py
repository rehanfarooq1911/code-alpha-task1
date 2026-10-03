import random

def play_hangman():
    word_list = ["google", "mango", "youtube", "fintech", "system"]    
    target_word = random.choice(word_list).lower()
    
    guessed_letters = []
    incorrect_guesses_left = 6 
    
    print("Welcome to Text-Based Hangman!")
    
    while incorrect_guesses_left > 0:
        display_word = ""
        for letter in target_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                
        print("\nWord:", display_word)
        print("Incorrect guesses remaining:", incorrect_guesses_left)
        
        if "_" not in display_word:
            print("Congratulations! You guessed the word: ", target_word)
            return
            
        guess = input("Guess a single letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter exactly one letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
            
        guessed_letters.append(guess)
        
        if guess not in target_word:
            print("Incorrect!", {guess},"is not in the word.")
            incorrect_guesses_left -= 1
        else:
            print("Good job!", {guess}, "is in the word.")
            
    print("\nGame Over! You ran out of guesses. The word was:", {target_word})

if __name__ == "__main__":
    play_hangman()
