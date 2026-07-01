# CodeAlpha Tasks

![Animated CodeAlpha Tasks banner](assets/hero.svg)

This repository contains two Python mini-projects built for CodeAlpha tasks:

- **Task-1**: a Streamlit-powered conversational chatbot called **H E R M I T**.
- **Task-2**: a command-line email extractor that scans text files and saves valid email addresses.

Both projects are small, focused, and practical. One demonstrates interactive UI and rule-based response handling, while the other shows file processing and regular-expression automation.

## Repository Structure

```text
codealpha_tasks/
├── Task-1/
│   ├── app.py
│   ├── chatbot.py
│   ├── requirements.txt
│   ├── README.md
│   └── About_Task.txt
├── Task-2/
│   ├── extract_emails.py
│   ├── sample_text.txt
│   ├── extracted_emails.txt
│   ├── README.md
│   └── About_Task.txt
└── assets/
    └── hero.svg
```

## Tasks At A Glance

| Task | Project | What It Does | Main Python Concepts |
| --- | --- | --- | --- |
| Task-1 | H E R M I T Chatbot | Opens a Streamlit chat interface and replies to greetings, questions, jokes, weather, time, and math prompts. | `if/elif`, functions, loops, APIs, Streamlit UI |
| Task-2 | Email Extractor | Reads a text file, extracts unique valid email addresses, and writes them to an output file. | `re`, file handling, command-line arguments, error handling |

## Task-1: H E R M I T Chatbot

Task-1 is a rule-based chatbot with two entry points:

- `chatbot.py` contains the core response logic and a terminal chat loop.
- `app.py` provides the Streamlit front end with a styled chat interface.

### Chatbot Highlights

- Responds to greetings, farewells, and common chatbot prompts.
- Can tell a joke.
- Can return local or location-based weather.
- Can return time for a location.
- Can evaluate math expressions, including some symbolic forms.
- Uses a neon-style Streamlit interface for a more polished experience.

### Run Task-1

Install the dependencies first:

```bash
pip install -r Task-1/requirements.txt
```

Run the Streamlit app:

```bash
streamlit run Task-1/app.py
```

Or run the terminal chatbot directly:

```bash
python Task-1/chatbot.py
```

## Task-2: Email Extractor

Task-2 is a lightweight automation script that extracts email addresses from text files and writes the unique results to a separate file.

### Extractor Highlights

- Uses a regex pattern to detect valid email addresses.
- Removes duplicates while keeping the original order.
- Works with default sample files or custom input/output paths.

### Run Task-2

Use the default sample files:

```bash
python Task-2/extract_emails.py
```

Or provide your own files:

```bash
python Task-2/extract_emails.py input.txt output.txt
```

## Requirements

- Python 3.x
- For Task-1: `streamlit`, `sympy`
- For Task-2: no third-party dependencies

## Notes

- Task-1 is best run with an internet connection because the weather and time features use external services.
- Task-2 is fully offline and depends only on local file input.
- Sample outputs and demonstration files are already included in the task folders.

## Author

Created for the CodeAlpha internship tasks by **Ashish Kumar**.
