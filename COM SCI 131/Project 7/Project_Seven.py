# Random Number File Reader

text = open("random.txt", "r")

# Opening Statement
print("The following numbers were read from the random.txt file: ")

sum = 0
count = 0

for line in text:
    print(line.strip())
    line = int(line)
    sum += line
    count += 1

print("The total of the numebers is:", str(sum))
print("The file contained", str(count), "numbers.")

text.close()
