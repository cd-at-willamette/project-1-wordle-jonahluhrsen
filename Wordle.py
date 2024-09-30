########################################
# Name: Jonah Luhrsen
# Collaborators (if any): None
# GenAI Transcript (if any): https://docs.google.com/document/d/1_vuUKUHLf1SlTJuoIQEhs9Gyml6cTgQB661oClXaKX8/edit#heading=h.hfl93vxo3pdz
# Estimated time spent (hr): 10
# Description of any added extensions: None
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        row_number = gw.get_current_row()
        
        guessed_word = ""
        for i in range(N_COLS):
            letter = gw.get_square_letter(row_number, i)
            guessed_word += letter
        
        if is_english_word(guessed_word) and len(str(guessed_word)) == 5: #seeing if the guess is an actual word
            affirmation = "In Word List"
            gw.show_message(affirmation)
            yellow_count = 0
            new_row = gw.get_current_row() + 1
            for i in range(N_COLS):
                letter_guessed = gw.get_square_letter(row_number, i)
                yellow_count = color_letter(row_number, i, letter_guessed, guessed_word, actual_word[i], actual_word, yellow_count)
        else: #if its not a real word it displays that to the user
            boo = "Not in word list" 
            gw.show_message(boo)
        guessed_word = ""
        gw.set_current_row(new_row)
        if row_number + 1 == N_ROWS: #if the user loses display a message
            loss = f"The Word Was {actual_word.upper()}"
            gw.show_message(loss)
            gw.set_current_row(N_ROWS)
            return
        if check_if_game_over(row_number):
            return
         
    def check_if_game_over(row_number): #if the user wins display a message
        if gw.get_square_color(row_number, 0) == CORRECT_COLOR and \
           gw.get_square_color(row_number, 1) == CORRECT_COLOR and \
           gw.get_square_color(row_number, 2) == CORRECT_COLOR and \
           gw.get_square_color(row_number, 3) == CORRECT_COLOR and \
           gw.get_square_color(row_number, 4) == CORRECT_COLOR:
            win = "WIN!"
            gw.show_message(win)
            gw.set_current_row(N_ROWS)
            return True
        return False
            
    def random_five_letter_word(): #defining the random word
        answer = random.shuffle(ENGLISH_WORDS)
        for word in ENGLISH_WORDS:
            if len(word) ==5:
                str_word = word.lower()
                return str_word
            
    def color_letter(row, column, letter_guessed, guessed_word, actual_letter, actual_word, yellow_count):
        actual_word = actual_word.lower()
        guessed_word = guessed_word.lower()
        letter_guessed = letter_guessed.lower()
        same = [False] * N_COLS
        
        for i in range(N_COLS): #mark correct letters
            if guessed_word[i] == actual_word[i]:
                gw.set_square_color(row, i, CORRECT_COLOR)
                change_key_color(guessed_word[i], CORRECT_COLOR)
                same[i] = True  #mark this letter as same

        for i in range(N_COLS): #mark present letters
            if guessed_word[i] != actual_word[i]:
                found_present = False
                for j in range(N_COLS):
                    if guessed_word[i] == actual_word[j] and not same[j]:
                        gw.set_square_color(row, i, PRESENT_COLOR)
                        change_key_color(guessed_word[i], PRESENT_COLOR)
                        same[j] = True #mark this letter as the same
                        yellow_count += 1
                        found_present = True
                        break
                if not found_present: #if not found as present, mark it as missing
                    gw.set_square_color(row, i, MISSING_COLOR)
                    change_key_color(guessed_word[i], MISSING_COLOR)
        return yellow_count

    def change_key_color(letter, color):
        current_color = gw.get_key_color(letter) #find the current color
        if current_color == UNKNOWN_COLOR: #update color
            gw.set_key_color(letter, color)
            return
        if current_color == CORRECT_COLOR: #leave correct color as correct color
            gw.set_key_color(letter, CORRECT_COLOR)
            return
        if current_color == PRESENT_COLOR and color == CORRECT_COLOR: #correct color overrides preset color
            gw.set_key_color(letter, CORRECT_COLOR)
            return
          
    actual_word = random_five_letter_word()

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup boilerplate
if __name__ == "__main__":
    wordle()


# Startup boilerplate
if __name__ == "__main__":
    wordle()
