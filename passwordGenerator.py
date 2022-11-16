import random

def replaceLetters(password) -> str:
    '''
    Purpose: To replace capital letters with numbers to be more secure
    Parameter(s):
        password: The password to change
    Return value: The new modified password
    '''
    lettersToReplace = {'I': 1, 'E' : 3, 'O': 0, 'S':5, 'B':8} #dict of letters to change
    newPass = ''#new password

    for char in password:#go through each character
        if char in lettersToReplace:#if its capital and in the letters to replace
            newPass += str(lettersToReplace[char])#replace
        else:
            newPass += char

    return newPass

def capOrNot(password) -> str:
    '''
    Purpose: To jumble capital letters or not
    Parameter(s):
        password: The imported password
    Return value: The same password with jumbled capital letters
    '''
    capital = 0#To determine if capital or not
    newPass = ''#The new password

    for char in password:#Go through each character
        capital = random.randint(0, 1)#50% chance of being capital or not
        if capital % 2 == 0:#if capital is even, uppercase, vice-versa
            newPass += char.upper()
        else:
            newPass += char.lower()

    return newPass#new password

def randomizer(words) -> str:
    '''
    Purpose: Randomize the words
    Parameter(s):
        words: A list of words that the user input
    Return value: A randomized string of words with random lowercase and uppercase
    '''
    password = '' #the final password
    randNum = 0 #generated number from 0-1
    usedWords = []#list of used words
    for i in range(len(words)):#go through each word
        while True:
            randNum = random.randint(0, len(words) - 1)#random word
            if randNum in usedWords:#if already used try again
                continue
            else:
                usedWords.append(randNum)
                password += words[randNum]#add to password if good
                break
    return replaceLetters(capOrNot(password))

def main() -> None:
    #Just a main method to run everything
    ans = ' '#Users input
    listOfWords = []#List of words to run through the randomizer
    while ans != '':
        ans = input('Please enter a word for your randomized password or simply click return to be finished: ')
        if ans != '':
            listOfWords.append(ans)
    print(f'Your randomized password: {randomizer(listOfWords)}')
    


main()


            



        
            
