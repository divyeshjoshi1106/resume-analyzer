import re


def extract_email(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)
    return list(set(email.lower() for email in emails))


def extract_phone(text):
    pattern = r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]"
    phone_numbers = re.findall(pattern, text)
    return list(set(num.strip() for num in phone_numbers))


def extract_links(text):
    pattern = (
        r"https?://(?:[a-zA-Z0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    )
    urls = re.findall(pattern, text)
    return list(set(urls))


def extract_name(text: str):
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    blocked_words = {
        "resume",
        "cv",
        "curriculum",
        "vitae",
        "email",
        "phone",
        "contact",
        "linkedin",
        "github",
        "profile",
        "summary",
    }

    for line in lines[:8]:
        lower_line = line.lower()

        if "@" in line or "http" in lower_line:
            continue

        if any(word in lower_line for word in blocked_words):
            continue

        if re.search(r"\d", line):
            continue

        words = line.split()

        if 2 <= len(words) <= 4 and all(word[0].isupper() for word in words if word):
            return line

    return None


def parse_resume_text(text: str) -> dict:
    return {
        "name": extract_name(text),
        "emails": extract_email(text),
        "phones": extract_phone(text),
        "links": extract_links(text),
    }
