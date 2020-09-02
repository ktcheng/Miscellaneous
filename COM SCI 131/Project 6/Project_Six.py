# Random Number File Writer
import random

# Opens text file to write random numbers
text = open("random.txt", "w")

# Opening Statement
opener = "This program writes random numbers to the random.txt file."
print(opener.strip())

count = float(input("How many numbers would you like to write: "))

# Integer validation check
while count % 1 != 0:
    count = float(input("Please enter a valid integer number: "))
count = int(count)

for i in range(count):
    text.write(str(random.randint(1, 501)))
    text.write("\n")

# Results Statement
final_line = (str(count), "numbers were written to the random.txt file.")
print(final_line.strip())

text.close()
