size = int(input("Enter the size of the pattern:"))


# Initialize row counter
row = 0

# Draw the Pattern
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after finishing a row
    row += 1