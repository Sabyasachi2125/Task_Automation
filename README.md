# Email Extractor Automation Script

This Python script automatically extracts email addresses from a text file and saves them into a separate file.

The program reads a file containing text, finds all email addresses using regular expressions, removes duplicates, and saves the results.

This project was developed as part of the **CodeAlpha Python Programming Internship**.

---

## Features

* Extracts email addresses from text files
* Uses Python regular expressions
* Removes duplicate emails
* Saves results to a new file
* Simple and easy to run

---

## Technologies Used

* Python
* Regular Expressions (`re`)
* File Handling

---

## How to Run

1. Place your text content in `input.txt`.

Example:

Hello contact us at [support@example.com](mailto:support@example.com)
You may also reach [admin@test.org](mailto:admin@test.org)

2. Run the script:

```bash
python email_extractor.py
```

3. The extracted emails will be saved in:

```
emails.txt
```

---

## Example Output

```
Extracted Email Addresses
-------------------------
support@example.com
admin@test.org
```
