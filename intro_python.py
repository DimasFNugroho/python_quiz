import json
import random
import openai

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

# Generate a new question using OpenAI
def generate_question(context):
    prompt = (
        f"Generate a Python-related multiple-choice question in strict JSON format. "
        f"The JSON should have the following keys:\n"
        f"'question' (string), 'options' (list of 4 strings), 'answer' (string), and 'explanation' (string).\n\n"
        f"Context: {context}\n\n"
        f"Example:\n"
        f"{{\n"
        f"  \"question\": \"What is the output of print('Hello World!')?\",\n"
        f"  \"options\": [\"a) Hello World!\", \"b) hello world!\", \"c) SyntaxError\", \"d) None\"],\n"
        f"  \"answer\": \"a\",\n"
        f"  \"explanation\": \"The print() function outputs the provided text exactly as given in quotes.\"\n"
        f"}}\n\n"
        f"Provide only the JSON as the output."
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates JSON-formatted questions."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7
    )

    response_text = response.choices[0].message.content.strip()

    # Validate and return the JSON
    try:
        question_dict = json.loads(response_text)
        return question_dict
    except json.JSONDecodeError:
        print("Error: Generated response is not valid JSON. Response received:")
        print(response_text)
        return None

def paraphrase_context(question_text):
    prompt = (
        f"Paraphrase the following question to make it slightly different but retain its meaning:\n"
        f"Original question: {question_text}\n\n"
        f"Paraphrased question:"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if available
        messages=[
            {"role": "system", "content": "You are a helpful assistant that paraphrases text."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# Modify questions interactively
def modify_questions():
    questions = load_questions()

    while True:
        print("\n--- Modify Questions ---")
        print("1. Add a New Question")
        print("2. Edit an Existing Question")
        print("3. Delete a Question")
        print("4. Regenerate All Questions")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            context = input("Provide the context for the new question: ").strip()
            print("\nGenerating a question based on the provided context...")
            question_dict = generate_question(context)
            if question_dict:
                questions.append(question_dict)
                print("Question added successfully!")
            else:
                print("Failed to generate a valid question. Please try again.")
        elif choice == "2":
            for i, q in enumerate(questions, start=1):
                print(f"\nQ{i}: {q['question']}")
            try:
                idx = int(input("\nEnter the number of the question you want to edit: ").strip()) - 1
                if idx < 0 or idx >= len(questions):
                    print("Invalid question number. Please try again.")
                    continue
                print(f"Selected question: {questions[idx]['question']}")

                # Automatically generate a new context
                print("\nGenerating a slightly different context based on the current question...")
                paraphrased_context = paraphrase_context(questions[idx]['question'])
                print(f"New context: {paraphrased_context}")

                print("\nGenerating an updated question...")
                question_dict = generate_question(paraphrased_context)
                if question_dict:
                    questions[idx] = question_dict
                    print("Question updated successfully!")
                else:
                    print("Failed to generate a valid question. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid question number.")
        elif choice == "3":
            for i, q in enumerate(questions, start=1):
                print(f"\nQ{i}: {q['question']}")
            try:
                idx = int(input("\nEnter the number of the question you want to delete: ").strip()) - 1
                if idx < 0 or idx >= len(questions):
                    print("Invalid question number. Please try again.")
                    continue
                confirm = input(f"Are you sure you want to delete question {idx + 1}? (yes/no): ").strip().lower()
                if confirm == "yes":
                    questions.pop(idx)
                    print("Question deleted successfully!")
            except ValueError:
                print("Invalid input. Please enter a valid question number.")
        elif choice == "4":
            print("\nRegenerating all questions...")
            regenerated_questions = []
            for i, q in enumerate(questions, start=1):
                print(f"\nRegenerating Q{i}: {q['question']}")
                try:
                    # Paraphrase context and generate a new question
                    paraphrased_context = paraphrase_context(q['question'])
                    print(f"New context: {paraphrased_context}")
                    regenerated_question = generate_question(paraphrased_context)
                    if regenerated_question:
                        regenerated_questions.append(regenerated_question)
                        print(f"Q{i} regenerated successfully!")
                    else:
                        print(f"Failed to regenerate Q{i}. Keeping the original.")
                        regenerated_questions.append(q)
                except Exception as e:
                    print(f"Error regenerating Q{i}: {e}")
                    regenerated_questions.append(q)  # Keep the original in case of failure
            questions = regenerated_questions
            print("All questions have been regenerated!")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

        # Save updated questions
        save_questions(questions)

# Quiz functionality
def test_intro_python():
    print("\n--- Intro to Python ---")

    # Load questions
    questions = load_questions()

    # Shuffle questions
    random.shuffle(questions)

    # Quiz loop
    score = 0
    for idx, q in enumerate(questions, start=1):
        print(f"\nQ{idx}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer: ").strip().lower()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! {q['explanation']}")

    print(f"\nYour score for Intro to Python: {score}/{len(questions)}")
    return score

# Main menu for this module
def main():
    while True:
        print("\n--- Intro Python Module ---")
        print("1. Take the Quiz")
        print("2. Modify Questions")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            test_intro_python()
        elif choice == "2":
            modify_questions()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

