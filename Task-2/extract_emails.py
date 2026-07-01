import re
import sys
import os

def extract_emails(input_file, output_file):
    # Regular expression for extracting email addresses (with word boundaries)
    email_regex = re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b')
    
    if not os.path.exists(input_file):
        print(f"Error: The input file '{input_file}' does not exist.")
        return

    try:
        # Read the content of the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
            
        # Find all email addresses in the text
        emails = email_regex.findall(text)
        
        # Remove duplicates while preserving order (optional, but usually desired)
        unique_emails = list(dict.fromkeys(emails))
        
        # Write the extracted emails to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            for email in unique_emails:
                file.write(email + '\n')
                
        print(f"Successfully extracted {len(unique_emails)} unique email addresses.")
        print(f"Saved to '{output_file}'.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Default files for demonstration
    input_file = 'sample_text.txt'
    output_file = 'extracted_emails.txt'
    
    # Allow passing arguments from command line
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    elif len(sys.argv) != 1:
        print("Usage: python extract_emails.py [input_file] [output_file]")
        sys.exit(1)

    extract_emails(input_file, output_file)
