# Popular Names

boy = open("BoyNames.txt", "r")
girl = open("GirlNames.txt", "r")

# Collects boy names from file
boy_list = []
for line in boy:
    boy_list.append(line.strip())

# Collects girl names from file
girl_list = []
for line in girl:
    girl_list.append(line.strip())

# Name popularity checker
while True:
    guess = input("Enter a name to check, or 'stop' to stop: ")
    
    if guess == "stop":
        break

    if (guess in boy_list) and (guess in girl_list):
        boy_rank = (boy_list.index(guess) + 1) # Accounts for index 0
        girl_rank = (girl_list.index(guess) + 1)
        
        print(guess.title(), "is a popular boys name and is ranked:", 
              str(boy_rank))
        print(guess.title(), "is a popular girls name and is ranked:", 
              str(girl_rank))
        
    elif guess in boy_list:
        boy_rank = (boy_list.index(guess) + 1) 
        print(guess.title(), "is a popular boys name and is ranked:", 
              str(boy_rank))
        print(guess.title(), "is not a popular girls name.")
        
    elif guess in girl_list:
        girl_rank = (girl_list.index(guess) + 1)
        print(guess.title(), "is a popular girls name and is ranked:", 
              str(girl_rank))
        print(guess.title(), "is not a popular boys name.")
            
    else:
        print(guess.title(), "is not a popular boys name.")
        print(guess.title(), "is not a popular girls name.")
        
boy.close()
girl.close()
