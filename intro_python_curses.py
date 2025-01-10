import curses
import json
import openai
import random

# Load API key from api_key.txt
def load_api_key():
    try:
        with open("api_key.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error: 'api_key.txt' file not found. Please create the file and add your OpenAI API key.")
        exit(1)
    except Exception as e:
        print(f"Error: Unable to load API key. Details: {e}")
        exit(1)

# Set your OpenAI API key here
openai.api_key = load_api_key()


# Load questions from the JSON file
def load_questions():
    with open("intro_python.json", "r") as file:
        return json.load(file)

# Save updated questions to the JSON file
def save_questions(questions):
    with open("intro_python.json", "w") as file:
        json.dump(questions, file, indent=4)

# Main menu using curses
def main_menu(screen):
    curses.curs_set(0)  # Hide cursor
    screen.clear()
    options = ["Take the Quiz", "Modify Questions", "Regenerate All Questions", "Exit"]
    current_option = 0

    while True:
        screen.clear()
        screen.addstr(0, 0, "--- Python Exercise Program ---", curses.A_BOLD | curses.A_UNDERLINE)

        # Display menu options
        for idx, option in enumerate(options):
            if idx == current_option:
                screen.addstr(idx + 2, 2, f"> {option}", curses.A_REVERSE)  # Highlight selected option
            else:
                screen.addstr(idx + 2, 2, f"  {option}")

        # Handle user input
        key = screen.getch()

        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(options) - 1:
            current_option += 1
        elif key in (curses.KEY_ENTER, 10, 13):  # Enter key
            if current_option == 0:
                take_quiz(screen)
            elif current_option == 1:
                modify_questions(screen)
            elif current_option == 2:
                regenerate_all_questions(screen)
            elif current_option == 3:
                break

# Take the quiz
def take_quiz(screen):
    screen.clear()
    questions = load_questions()
    random.shuffle(questions)
    score = 0

    for idx, question in enumerate(questions, start=1):
        screen.clear()
        screen.addstr(0, 0, f"Question {idx}: {question['question']}", curses.A_BOLD)

        # Display options with highlighting
        current_option = 0
        while True:
            for i, option in enumerate(question["options"]):
                if i == current_option:
                    screen.addstr(i + 2, 2, f"> {chr(97 + i)}) {option}", curses.A_REVERSE)
                else:
                    screen.addstr(i + 2, 2, f"  {chr(97 + i)}) {option}")

            # Handle user input
            key = screen.getch()
            if key == curses.KEY_UP and current_option > 0:
                current_option -= 1
            elif key == curses.KEY_DOWN and current_option < len(question["options"]) - 1:
                current_option += 1
            elif key in (curses.KEY_ENTER, 10, 13):  # Enter key
                break  # Confirm choice

        # Check if the selected option is correct
        selected_answer = chr(97 + current_option)  # 'a', 'b', 'c', etc.
        if selected_answer == question["answer"]:
            score += 1
            screen.addstr(len(question["options"]) + 4, 0, "Correct!", curses.A_BOLD)
        else:
            screen.addstr(
                len(question["options"]) + 4, 0,
                f"Wrong! Correct answer: {question['answer']}. {question['explanation']}",
                curses.A_BOLD
            )

        screen.addstr(len(question["options"]) + 6, 0, "Press any key to continue...")
        screen.refresh()
        screen.getch()  # Wait for key press before moving to the next question

    # Display the final score
    screen.clear()
    screen.addstr(0, 0, f"Your score: {score}/{len(questions)}", curses.A_BOLD)
    screen.addstr(2, 0, "Press any key to return to the main menu...")
    screen.getch()

# Modify questions
def modify_questions(screen):
    screen.clear()
    screen.addstr(0, 0, "Modify Questions is not yet implemented with ncurses.", curses.A_BOLD)
    screen.addstr(2, 0, "Press any key to return to the main menu...")
    screen.getch()

# Regenerate all questions
def regenerate_all_questions(screen):
    screen.clear()
    screen.addstr(0, 0, "Regenerate All Questions is not yet implemented with ncurses.", curses.A_BOLD)
    screen.addstr(2, 0, "Press any key to return to the main menu...")
    screen.getch()

# Main entry point
def main():
    curses.wrapper(main_menu)

if __name__ == "__main__":
    main()

