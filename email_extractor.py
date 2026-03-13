import re


def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None


def extract_emails(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
    found_emails = re.findall(email_pattern, text)
    unique_emails = list(dict.fromkeys(found_emails))
    return unique_emails


def save_emails(filename, emails):
    with open(filename, "w") as file:
        for email in emails:
            file.write(email + "\n")


def main():
    input_text = read_file("input.txt")

    if input_text is None:
        return

    emails = extract_emails(input_text)

    print("Extracted Email Addresses")
    print("-------------------------")

    if not emails:
        print("No email addresses found.")
    else:
        for email in emails:
            print(email)

    save_emails("emails.txt", emails)
    print("\nEmails saved to emails.txt")


if __name__ == "__main__":
    main()
