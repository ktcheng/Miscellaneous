# List Number Analysis

file = open("random.txt", "r")

# Sorted list of numbers
num = []
for line in file:
    num.append(int(line.strip()))
num.sort()

print("The following numbers were read from the random.txt file: ")
print(*num, sep = "\n") # Prints every number on separate line

print("The lowest number in the list is: " + str(num[0]))
print("The highest number in the list is: " + str(num[-1]))
print("The total of the numbers is: " + str(sum(num)))

raw_avg = (sum(num)) / (len(num))
avg = round(raw_avg, 1)
print("The average of the numbers in the list is: " + str(avg))

file.close()
