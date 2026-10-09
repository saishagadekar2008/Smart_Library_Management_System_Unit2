"""Tuple Demonstration - Unit 2"""

isbn = ("978", "0134685991")
print("ISBN tuple:", isbn)

prefix, code = isbn
print("Unpacked prefix:", prefix)
print("Unpacked code:", code)

publication = (2020, "3rd Edition", "Pearson")
year, edition, publisher = publication
print("Year:", year)
print("Edition:", edition)
print("Publisher:", publisher)

print("Count of 978:", isbn.count("978"))
print("Index of 0134685991:", isbn.index("0134685991"))

print("Tuples are immutable. The following would cause an error if uncommented:")
print("# isbn[0] = '979'")
