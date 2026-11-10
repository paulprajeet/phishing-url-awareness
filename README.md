# Phishing URL Awareness Checker

## About
The Phishing URL Awareness Checker is a beginner-friendly Python cybersecurity project that identifies common warning signs in URLs.

It helps users understand suspicious URL characteristics without opening or visiting the websites.

## Features
- Detects the `@` symbol in URLs.
- Checks URL length greater than 100 characters.
- Identifies IPv4-looking hostnames.
- Detects hostnames with five or more segments.
- Identifies punycode markers (`xn--`).
- Detects HTTP URLs.
- Supports continuous URL input.
- Handles malformed URL input.

## Technologies Used
- Python 3.14.10
- Regular Expressions (`re`)
- URL Parsing (`urllib.parse`)
- Visual Studio Code

## Requirements
Python 3.10 or later.

No external Python packages are required.

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Execute:

```bash
python phishing_checker.py
```

5. Enter a URL to analyze.
6. Type `quit` to exit.

## Testing
Five sample URLs were used for manual testing.

Refer to `tests/test_samples.md` for test cases and results.

## Project Structure

```text
phishing-url-awareness/
├── phishing_checker.py
├── README.md
├── requirements.txt
├── tests/
│   └── test_samples.md
└── screenshots/
    ├── sample_run.png
    └── test_results.png
```

## Limitations
- Does not visit or scan websites.
- Does not verify website ownership or reputation.
- Does not guarantee that a URL is safe.
- Detects only the warning signs implemented in the program.

## Ethical Use
This project is intended for cybersecurity education and awareness.

## Author
PAUL PRAJEET
