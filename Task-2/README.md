# Email Extractor Script

A simple and efficient Python script designed to automatically parse text files and extract all unique, valid email addresses. 

This project was built as part of the CodeAlpha Internship task for "Task Automation with Python Scripts".

## Features

- **Accurate Extraction:** Uses a robust Regular Expression (Regex) to correctly identify valid email addresses while ignoring broken or partial ones.
- **Duplicate Removal:** Automatically filters out duplicate email addresses, outputting a clean and unique list.
- **Command-Line Interface:** Can be run with custom input and output file paths directly from your terminal.

## Prerequisites

- Python 3.x installed on your system.
- No external libraries required (relies purely on Python's built-in `re`, `sys`, and `os` modules).

## Usage

### 1. Default Demonstration
By default, the script reads from the provided `sample_text.txt` and outputs the extracted emails to `extracted_emails.txt`. Just run:

```bash
python extract_emails.py
```

### 2. Custom Files
You can easily specify your own input and output files by passing them as arguments in the terminal:

```bash
python extract_emails.py <input_file.txt> <output_file.txt>
```

**Example:**
```bash
python extract_emails.py customer_data.txt clean_emails.txt
```

## How It Works

1. The script reads the entire text from the specified input file.
2. It applies a RegEx pattern with word boundaries to match all email-like strings.
3. It removes any duplicates while keeping the original order.
4. It writes the final list of emails to the specified output file, one per line.
"# CodeAlpha_Task-Automation-with-Python-Scripts" 
