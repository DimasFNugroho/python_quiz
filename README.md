# Python Quiz Application

An interactive Python quiz application designed to help you practice and improve your Python programming skills. This project leverages `ncurses` for a clean and interactive console UI and integrates the OpenAI API for dynamic question generation.

---

## Features

- **Interactive Console UI**: Navigate through the application using a clean menu system powered by `ncurses`.
- **Dynamic Question Generation**: Uses OpenAI's GPT models to generate and update Python-related quiz questions.
- **Customizable Question Bank**: Add, edit, delete, or regenerate questions with ease.
- **Bulk Regeneration**: Refresh all questions in the database with new, paraphrased contexts.
- **Scoring System**: Tracks and displays your quiz score with real-time feedback for correct and incorrect answers.
- **Modular Design**: Easy to extend and customize the application.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (place it in `api_key.txt`)

### Clone the Repository

```bash
git clone https://github.com/DimasFNugroho/python_quiz.git
cd python_quiz
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

1. **Add Your OpenAI API Key**:
   - Create a file named `api_key.txt` in the root directory.
   - Paste your OpenAI API key into the file.

   Example:
   ```plaintext
   sk-your-openai-api-key-here
   ```

2. **Question Database**:
   - Questions are stored in `intro_python.json`.
   - You can pre-populate the file with your own questions or let the app generate them dynamically.

---

## Usage

### Run the Application

```bash
python3 intro_python_curses.py
```

### Menu Options

1. **Take the Quiz**:
   - Answer Python-related multiple-choice questions.
   - Navigate using arrow keys and confirm your selection with Enter.
   - Receive real-time feedback and track your score.

2. **Modify Questions**:
   - Add, edit, or delete questions in the question bank.

3. **Regenerate All Questions**:
   - Refresh all questions in the database with paraphrased contexts and new dynamically generated questions.

4. **Exit**:
   - Quit the application.

---

## File Structure

- `intro_python_curses.py`: Main application script with an interactive `ncurses` interface.
- `intro_python.json`: JSON file storing the question database.
- `api_key.txt`: File storing the OpenAI API key.
- `requirements.txt`: List of dependencies required for the project.
- `README.md`: Project documentation.

---

## Dependencies

The project relies on the following Python libraries:

- `curses` (built-in for Linux/Mac; installable via `windows-curses` for Windows)
- `openai`

To install all dependencies:

```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or new features.

---

## License

This project is licensed under the [GPL-3.0 License](https://www.gnu.org/licenses/gpl-3.0.en.html). You are free to use, modify, and distribute this project under the terms of the license.

---

## Author

- **Dimas Fajrian Nugroho**  
  GitHub: [DimasFNugroho](https://github.com/DimasFNugroho)

---

## Acknowledgments

- Thanks to [OpenAI](https://openai.com) for providing powerful APIs for dynamic question generation.
- Inspired by the need for interactive and engaging programming exercises.

---

Start your Python learning journey today with this quiz application! 🚀

