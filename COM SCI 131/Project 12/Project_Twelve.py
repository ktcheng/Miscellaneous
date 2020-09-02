# Popular Name With Functions

# Opening Statement
print("Enter a name to see if it is a popular girls or boys name.")

def file_opener(filename):
    with open(filename, "r") as file:
        # Collect all names
        nameList = []
        for line in file:
            nameList.append(line.strip())

    return nameList

def checkName(name, nameList):
    rank = 0
    if name in nameList:
        rank = nameList.index(name) + 1
    return rank

while True:
    name = input("Enter a name to check, or 'stop' to stop: ")
    
    if name == "stop":
        break
    
    boy, girl = (file_opener("BoyNames.txt"), file_opener("GirlNames.txt"))
    b, g = (checkName(name, boy), checkName(name, girl))
    
    if b != 0 and g != 0: # Popular boy & girl name
        print(name.title() + " is a popular girls name and is ranked:", str(g))
        print(name.title() + " is a popular boys name and is ranked:", str(b))
        
    elif g != 0: # Popular girl name
        print(name.title() + " is a popular girls name and is ranked:", str(g))
        print(name.title() + " is not a popular boys name.")
        
    elif b != 0: # Popular boy name
        print(name.title() + " is not a popular girls name.")
        print(name.title() + " is a popular boys name and is ranked:", str(b))
        
    else: # Not popular name
        print(name.title() + " is not a popular girls name.")
        print(name.title() + " is not a popular boys name.")
