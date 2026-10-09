"""Set Operations - Unit 2"""

categories = ["Fiction", "Sci-Fi", "Fiction", "History"]
unique_categories = set(categories)
print("Unique categories:", unique_categories)

fiction_readers = {"Aisha", "Ben", "Chen"}
scifi_readers = {"Ben", "Divya"}

print("Union:", fiction_readers | scifi_readers)
print("Intersection:", fiction_readers & scifi_readers)
print("Difference:", fiction_readers - scifi_readers)

unique_categories.add("Programming")
print("After add:", unique_categories)

unique_categories.discard("History")
print("After discard:", unique_categories)

print("'Fiction' in categories:", "Fiction" in unique_categories)
