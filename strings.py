"""String Programming Exercises - Unit 2"""

title = "  the great gatsby  "
author = "f. scott fitzgerald"
text = "Python is useful. Python is easy."

print("Original:", title)
print("upper():", title.upper())
print("lower():", author.lower())
print("title():", title.strip().title())
print("capitalize():", author.capitalize())
print("strip():", title.strip())
print("split():", "Fiction,Sci-Fi,History".split(","))
print("join():", ", ".join(["Fiction", "Sci-Fi", "History"]))
print("replace():", "Dune".replace("u", "o"))
print("find():", "library".find("brar"))
print("count():", "banana".count("a"))
print("startswith():", "1984".startswith("19"))
print("endswith():", "Emma.pdf".endswith(".pdf"))

def validate_isbn(isbn):
    digits_only = isbn.replace("-", "")
    return digits_only.isdigit() and len(digits_only) == 13

print("ISBN validation:", validate_isbn("978-0-13-468599-1"))
