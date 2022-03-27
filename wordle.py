import random
import copy
from colorama import Fore, Back
def Wordle(num):
    print("To play the game you will try to guess a valid word that is as long as the number that you had put in the start.")
    load=open(str(num)+"letterwords.txt","r").read().split("\n")
    #print(load)
    word_index=int(random.uniform(0,len(load)-1))
    o_word=list(load[word_index])
    o_word="wrong"
    #print(word)
    #print(word)
    print("You will have 6 guesses")
    print("Everytime you guess a word you will see if each letter is in the correct place or not.")
    print("+ and the color green means the letter is in the right location")
    print("- and the color black means the letter is not in the word")
    print("| and the color yellow means the letter exists in the word but it is not in the correct location")
    print("You can ask the computer to tell all the words that have some letters in them")
    rotation=1
    l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    apla=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cor=[]
    yel=[]
    guess_word="r"
    found=[]
    gre=[]
    display=[]
    accepted={"z"}
    accepted.remove("z")
    rejected={"z"}
    rejected.remove("z")
    word=list(copy.deepcopy(o_word))
    while rotation!=7 and guess_word!=list(o_word):
        gre=[]
        word=list(copy.deepcopy(o_word))
        #print('display:' + str(display))
        for i in range(rotation-1):
            print("\n"+display[num*(i)],end=" ")
            for j in range(num-1):
                print(display[(num*(i))+j+1],end=" ")
        guess_word=input("\nPut a valid word\n").lower()
        while guess_word not in load :
            guess_word=input("Put a valid word, this is not a valid word and/or the length of your word is wrong.\n").lower()
        guess_word=list(guess_word)
        for x in range(num):
            #print(x)
            #print(word)
            if guess_word[x] in apla:
                apla.remove(guess_word[x])
            if guess_word[x]==word[x]:
                found.append(guess_word[x])
                cor.append(guess_word[x])
                #print(Back.GREEN+"+" + Back.RESET,end="")
                #print(x)
                gre.append((Back.GREEN+"+" + Back.RESET,x))
                #print('green:'+ str(display))
                accepted.add(guess_word[x])
                word[x]=""
        for x in range(num):
            if (Back.GREEN+"+" + Back.RESET,x) in gre:
                print(Back.GREEN+"+"+ Back.RESET,end="")
                display.append(Back.GREEN+guess_word[x].upper() + Back.RESET)
            elif (word[x]!=""):
                #print(str(guess_word[x] in word) + " " + str(word[x]!="x")) 
                if guess_word[x] in word:
                    print(Back.YELLOW+"|"+ Back.RESET,end="")
                    yel.append(guess_word[x])
                    display.append(Back.YELLOW+ guess_word[x].upper() + Back.RESET)
                    #print('yellow:'+str(display) +',' + str(word.index(guess_word[x])) + " " +word[word.index(guess_word[x])])
                    word[word.index(guess_word[x])]="x"
                    accepted.add(guess_word[x])
                else:
                    print(Back.BLACK+"-" + Back.RESET,end="")
                    display.append(Back.BLACK+guess_word[x].upper() + Back.RESET)
                    #print('black:'+ str(display))
                    if guess_word[x] not in accepted:
                        rejected.add(guess_word[x])
        rotation+=1
        if guess_word!=list(o_word) and rotation!=7:
            print("\nThe letter representaion so far is:",end=" ")
            for x in l:
                if x in cor:
                    print(Back.GREEN+x + Back.RESET,end="")
                elif x in yel:
                    print(Back.YELLOW+x + Back.RESET,end="")
                else:
                    print(Back.BLACK+x + Back.RESET,end="")
            print("\nYou have "+ str(7-rotation) +" guesses left")
            foun=False
            ifclue=input("Do you want to see words that have some letters that you put in? please put yes or no: ")
            while (ifclue == "yes" or ifclue == "Yes" or ifclue == "YES" or ifclue == "y" or ifclue == "Y"):
                letters=input("Enter the letters seperated by commas: ").split(",")
                for words in list(load):
                    ifin=True
                    for g in letters:
                        x=g.strip()
                        #print(g)
                        #print(x)
                        if x not in words:
                            ifin = False
                    for d in rejected:
                        if d in words:
                            ifin=False
                    if ifin==True:
                        foun=True
                        print(words)
                #print(letters)
                if foun==False:
                    print("no words")
                ifclue=input("Do you want to see words that have some letters that you put in? ")

    if rotation==7:
        print("I am sorry but you lost, the word was " + str(o_word))
    else:
        print("\nNice Job! you were able to get the word in " + str(rotation-1) + " guesses")
    print("Thank you for playing!")
print("############################################################")
print("############################################################")
print("Welcome to Krish's variation of the popular fun game: Wordle")
print("My version of Wordle is called KRINIKA-WORDLE")
print("############################################################")
print("############################################################")
print("#   KRINIKA-WORDLE    KRINIKA-WORDLE     KRINIKA-WORDLE    #")
print("############################################################")
print("############################################################")
value=int(input("Please choose a integer between 4 and 8. That is the number of alphabets in the computer generated word that you will guess. \n"))
while (value<4 or value>8) :
    value=int(input("Please choose a integer between 4 and 8. That is the number of alphabets in the computer generated word that you will guess. \n"))
print("Have a good game !")
Wordle(value)