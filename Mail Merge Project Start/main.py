#TODO: Create a letter using starting_letter.txt
with open(r"./Input/Letters/starting_letter.txt", "r") as templateletter:
    newletter = templateletter.read()
    with open(r"./Input/Names/invited_names.txt") as names:
        names = names.readlines()
        for item in names:
            name = item.strip("\n")
            print(newletter)
            newletterwithname = newletter.replace("[name]", name)
            f = open(rf"./Output/ReadyToSend/letter_for_{name}.txt", mode="w")
            f.write(newletterwithname)
            f.close()
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp