"""List Management Exercises - Unit 2"""

books = ["1984", "Dune", "Emma"]
print("Initial list:", books)

books.append("Atomic Habits")
books.insert(0, "The Alchemist")
books.extend(["Python Crash Course", "Clean Code"])
print("After append/insert/extend:", books)

print("index of Dune:", books.index("Dune"))
print("count of Dune:", books.count("Dune"))

books.remove("Emma")
removed = books.pop(0)
print("Removed by pop:", removed)

books.sort()
print("Sorted:", books)

books.reverse()
print("Reversed:", books)

long_titles = [title for title in books if len(title) > 4]
print("Titles longer than 4 characters:", long_titles)

temp = books.copy()
temp.clear()
print("After clear on copy:", temp)
