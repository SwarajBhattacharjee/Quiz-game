# Quiz Game
[![CI](https://github.com/yourusername/quiz-game/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/quiz-game/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/yourusername/quiz-game/blob/main/LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/quiz-game)](https://pypi.org/project/quiz-game)


Welcome to **Quiz Game**, a simple, interactive true/false quiz application built in Python. Questions are sourced via the Open Trivia Database (OpenTDB) API and organized into different categories. Users can choose how many questions to answer and receive immediate feedback on their responses.

---

## Table of Contents

1. [Features](#features)
2. [Built With](#built-with)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [API Integration](#api-integration)
8. [Advanced Usage](#advanced-usage)
9. [Screenshots](#screenshots)
10. [Contributing](#contributing)
11. [Code of Conduct](#code-of-conduct)
12. [License](#license)
13. [Contact](#contact)

---

## Features

* Multiple question sets: Animal, Basic True/False, Extended Trivia
* Dynamic selection of quiz length (10, 12, or 60 questions)
* Immediate feedback on correct/incorrect answers
* Score tracking throughout the quiz

## Built With

* Python 3.x
* Standard Library Modules (`json`)
* [requests](https://pypi.org/project/requests/) for API calls

## Prerequisites

* Python 3.7 or later installed on your system
* A terminal/command prompt
* Internet connection to fetch quiz questions

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/quiz-game.git
   ```
2. Change into the project directory:

   ```bash
   cd quiz-game
   ```
3. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate     # On Windows use: venv\\Scripts\\activate
   ```
4. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you are in the project directory.
2. Run the main program:

   ```bash
   python main.py
   ```
3. When prompted, choose how many questions you want to play by entering `10`, `12`, or `60`.
4. Answer each question by typing `True` or `False` and pressing Enter.
5. View your score at the end of the quiz.

## Project Structure

```plaintext
quiz-game/
│
├── data.py             # Static question sets and API response example
├── main.py             # Entry point: orchestrates quiz flow
├── question_model.py   # Question class definition
├── quiz_brain.py       # Logic for asking questions and tracking score
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## API Integration

This project uses the [Open Trivia Database API](https://opentdb.com/api_config.php) to retrieve questions dynamically. In your `data.py` file, you’ll explicitly import the HTTP GET function from `requests`:

```python
from requests import get

# Example: fetch 10 boolean questions from the Animals category (category ID 27)
response = get('https://opentdb.com/api.php?amount=10&type=boolean&category=27')
Animal_question_data = response.json()
```

The application will parse the JSON response and convert each question into a `Question` object. No further changes to the core logic are required.

## Advanced Usage

* **Custom Category/Type**: Modify the API URL in `data.py` to change `amount`, `category`, or `type` parameters.
* **Persistent Scores**: Extend the project to save high scores to a file or database.
* **Multiple Choice**: Adapt parsing logic to handle `multiple` question types (`type=multiple`).
* **GUI Integration**: Build a graphical interface using Tkinter or PyQt.

## Screenshots

![Quiz Game Demo](docs/screenshot.gif)
*Animated demo showing quiz flow and scoring.*

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines. In short:

1. Fork the repository.
2. Create your feature branch:

   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add some amazing feature"
   ```
4. Push to the branch:

   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request.

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Created by Swaraj Bhattacharjee. Feel free to reach out with questions or suggestions at [your.email@example.com](mailto:your.email@example.com).
