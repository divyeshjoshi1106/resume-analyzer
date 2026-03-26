import re


def extract_email(text):
    email = re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
    return email.group(0)


def extract_phone(text):
    pass


def extract_links(text):
    pass


def extract_links(text):
    pass


def parse_resume_text(text: str) -> dict:
    return {"name": ..., "email": ..., "phone": ..., "links": ...}


mytext = """
    HI, my name is divyesh.
if you have any issues, contact me at 123@abc.com
"""

print(extract_email(mytext))
