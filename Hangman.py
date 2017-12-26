'''
Erika Fortune
11.8.17
Purpose: To perform the game of Hangman
'''
from random import*

def guessLetter(letter,newList,wordList,incorrect,correct,word):
    '''
    Args: the letter the player guessed and the word selected from selectList
    Return: where the the letter belongs in the word or what body part to draw  
    Purpose: To find if the letter that the player guessed is in the word or not
    '''        
    notinword=True
    if(correct==(len(wordList))):
        print("You win")
    else:
        for x in range(len(wordList)):

            if(wordList[x]==letter):
                newList[x]=wordList[x]
                notinword=False
        print(" ".join(newList))
    
    if(notinword):
        return failedGuess(incorrect,word)
    return incorrect
def getCorrect(newList,wordList):
    '''
    Args:NewList and wordlist
    Return: True or false
    Purpose: To decide if the list that contains the player's correct guesses equalled the list containing the random word selected    
    '''
    if (newList==wordList):
        print("You Win!!")
        return True
    else:
        return False
   
def failedGuess(incorrect,word):
    '''
    Arg: the letter that was not in the word
    Return: the body part in which should be printed
    Purpose: to find the next body part to printed depending on how many failed
    guesses the player has had

    note: included help from Aaron Segal for this function
    '''

    incorrect=incorrect+1
    if incorrect==1:
        print("head")
    elif incorrect==2:
        print("head,", "body")
    elif incorrect==3:
        print("head,","body,","right arm")
    elif incorrect==4:
        print("head,","body,","right arm,","left arm")
    elif incorrect==5:
        print("head,","body,","right arm,","left arm,", "right leg")
    elif incorrect==6:
        print("head,","body,","right arm,", "left arm,", "right leg,","left leg")
    elif incorrect==7:
        print("Sorry, You have lost. The word was",word)
    return incorrect
def getSpace(word):
    '''
    Args: word
    Return: the newList aka space per letter in the word that was randomly chosen
    Purpose: to print a space per character in the word that was randomly chosen
    '''
    newList=[]
    space=('_')
    wordList=word.split(word)
    for x in range(len(word)):
        newList.append(space)
    return newList
    
                
def main():
    correct=0
    incorrect=0
    selectList=["dog","cat","mouse","rat","pig","goat","penguin","parrot"]
    print("Welcome to the game of Hangman. Here is your word:")
    word=selectList[randint(0,5)]
    newList=getSpace(word)
    print(" ".join(newList))
    win=False
    wordList=[]
    for x in range(len(word)):
        wordList.append(word[x])
    
    while((incorrect<7) and (win==False)):
        letter=input("Guess a letter: ")
        incorrect=guessLetter(letter,newList,wordList,incorrect,correct,word)
        win=getCorrect(newList,wordList)  
    
main()
