# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

with open("records.txt", "w") as f:
    f.write("R-007\n"),
    f.write("R-004\n"),
    text = f.read()

print(text)
    


