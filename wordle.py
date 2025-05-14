from words import read_word_list
import time
import keyboard
import pyautogui
from typing import List, Tuple

def enter_word(word: str):
    """Types the word and presses enter with delays to match game animations"""
    time.sleep(0.5)  # Wait for game to be ready
    pyautogui.write(word, interval=0.1)  # Type word with slight delays
    pyautogui.press('enter')
    time.sleep(2)  # Wait for animations

def wait_between_guesses(delay: float = 2.0):
    """Waits between guesses with a progress indicator"""
    print("Waiting for animations...", end="")
    for _ in range(int(delay * 2)):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

def play(possible_guesses: List[str], possible_answers: List[str]):
    words = possible_guesses
    narrowed_down_list = possible_answers

    print("\nInstructions:")
    print("1. Open https://www.nytimes.com/games/wordle/index.html in your browser")
    print("2. Make sure the game window is visible")
    print("3. Close any popups or dialogs")
    print("\nPress 'esc' when ready to start")
    keyboard.wait('esc')
    time.sleep(1)

    for guess_number in range(6):
        min_wordcount = 2e5
        chosen_word = ""
        evaluation_to_wordlist_map = {}
        
        if guess_number != 0:
            words_to_consider = words
        else:
            words_to_consider = ["arise"]  # First guess is always 'arise'
            
        # Find best word
        for word_to_guess in words_to_consider:
            temp_eval_to_words_map = {}
            
            for possible_answer in narrowed_down_list:
                evaluation = get_evaluation(possible_answer, word_to_guess)
                
                if tuple(evaluation) not in temp_eval_to_words_map:
                    temp_eval_to_words_map[tuple(evaluation)] = [possible_answer]
                else:
                    temp_eval_to_words_map[tuple(evaluation)].append(possible_answer)
    
            biggest_possible_remaining_wordcount = max([len(val) for val in temp_eval_to_words_map.values()])

            if biggest_possible_remaining_wordcount < min_wordcount:
                min_wordcount = biggest_possible_remaining_wordcount
                chosen_word = word_to_guess
                evaluation_to_wordlist_map = temp_eval_to_words_map

        # Automatically enter the word in Wordle
        print(f"\nEntering word: {chosen_word}")
        pyautogui.click()  # Ensure window is focused
        enter_word(chosen_word)
        wait_between_guesses()  # Wait for animations

        # Get color pattern from user
        while True:
            try:
                print("\nEnter the color pattern (5 digits):")
                print("Grey = 0, Yellow = 1, Green = 2")
                evaluation = input("> ")
                if len(evaluation) != 5 or not all(c in '012' for c in evaluation):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input! Please enter exactly 5 digits (0, 1, or 2)")

        answer_evaluation = tuple(int(x) for x in evaluation)

        # Process evaluation and update word list
        if answer_evaluation in evaluation_to_wordlist_map:
            narrowed_down_list = evaluation_to_wordlist_map[answer_evaluation]
            print(f"Possible words remaining: {len(narrowed_down_list)}")
            
        if answer_evaluation == (2, 2, 2, 2, 2):
            print(f"\nCongratulations! The word was: {chosen_word}")
            return
        
        if len(narrowed_down_list) == 1:
            final_word = narrowed_down_list[0]
            print(f"\nOnly one word possible: {final_word}")
            print("Entering final answer...")
            pyautogui.click()  # Ensure window is focused
            enter_word(final_word)  # Enter the final word
            print("This must be the answer!")
            return

        if len(narrowed_down_list) == 0:
            print("\nError: No possible words match this pattern")
            return

def get_evaluation(answer, word):
    # 0 = nothing, 1 = yellow, 2 = green
    output = [0, 0, 0, 0, 0]
    
    # check for correct letter and placement
    for i in range(5):
        if word[i] == answer[i]:
            output[i] = 2
            answer = answer[:i] + ' ' + answer[i + 1:]
           
    # check for correct letter
    for i in range(5):
        char = word[i]
        if char in answer and output[i] == 0:
            output[i] = 1
            first_occurence = answer.find(char)
            answer = answer[:first_occurence] + ' ' + answer[first_occurence + 1:]
    return tuple(output)

def main():
    print("Welcome to Wordle Solver!")
    print("=" * 50)
    possible_words = read_word_list()
    play(possible_words, possible_words)
    print("\nGame finished! Press 'esc' to exit")
    keyboard.wait('esc')

if __name__ == "__main__":
    main()