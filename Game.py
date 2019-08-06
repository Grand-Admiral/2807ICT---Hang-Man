#////////////////////--Student's Names: Krishna Punugu (s5054875), Jack Leyden (s5052939)--/////////////////////////
import sys, os, time
#vNO = 19
# Notes:
#this may not work when starting to read the file. solution is to get as much completed if the read dosn't work here.

#To test you must load it on your computer.

#must learn how to read a file (dictionary.txt)

#Settings
Length = None #lenght of words that the user wants to play with
letter = None #the letter that the user recently gussed, this will change pr guess
guess = None #letter
#----------------------------------------------------------------------
lists = ["",""] #needs to be used! have the words stored here and then cleared and stored again only when they fit a certain category.
Round = 0
#----------------------------------------------------------------------
counter = 0
counter2 = 0
counts = 2
gameover = False
Words_left = 0

#can use a list

def call(Length,guess):
# this calls the text and compares the text to the number selected
#for characters. ATM it then prints all the options
    try: 
        words = open("Dictionary.txt")
    except:
        print("Dictionary cannot be found")
        sys.exit()
    global lists
    global counter
    global counts
	#List
    global guess1
	#List remove soon
###
    global Oguess
    guess1[0] = guess
    
    global gameover
    global counter2
    global Words_left
    #theword = ""
    
	#here its selecting words
    for words in words.readlines(): 
#-------------------------------------------------------------------
# won't be nessesary 
        global Round
        words = words.strip()
            #words = lists

            #needs to add words to list
	    #here its stripping the "\n" char at the end of every line and it  gets stored in the var lists
            #print(lists), where words is the var that stores all the words in a line.
#-------------------------------------------------------------------
        theword = "" #Word --E-

        if Length == int(len(words.strip())):
#change guess to originalGuess
            if Oguess in words.strip():
            
                #find possible combinations
                #print(words.strip())
            
                for i in range(0, len(words.strip())):
                #print(words.strip()[i])

                
                #must have a loop somehow [Can Use List]
                #only remembers 2 letters could have 26 guesses for the alphabet?
                #have a counter that remembers which guess to store the letter in.
                    #for s in range(0,28):
                    
                    if words.strip()[i] == guess1[0]: #0
                        theword = str(theword) + guess1[0]
                    elif words.strip()[i] == guess1[1]: #1
                        theword = str(theword) + guess1[1]
                    elif words.strip()[i] == guess1[2]: #2
                        theword = str(theword) + guess1[2]
                    elif words.strip()[i] == guess1[3]: #3
                        theword = str(theword) + guess1[3]
                    elif words.strip()[i] == guess1[4]: #4
                        theword = str(theword) + guess1[5]
                    elif words.strip()[i] == guess1[5]: #5
                        theword = str(theword) + guess1[5]
                    elif words.strip()[i] == guess1[6]: #6
                        theword = str(theword) + guess1[6]
                    elif words.strip()[i] == guess1[7]: #7
                        theword = str(theword) + guess1[7]
                    elif words.strip()[i] == guess1[8]: #8
                        theword = str(theword) + guess1[8]
                    elif words.strip()[i] == guess1[9]: #9
                        theword = str(theword) + guess1[9]
                    elif words.strip()[i] == guess1[10]: #10
                        theword = str(theword) + guess1[10]
                    elif words.strip()[i] == guess1[11]: #11
                        theword = str(theword) + guess1[11]
                    elif words.strip()[i] == guess1[12]: #12
                        theword = str(theword) + guess1[12]
                    elif words.strip()[i] == guess1[13]: #13
                        theword = str(theword) + guess1[13]

                    elif words.strip()[i] == guess1[14]: #14
                        theword = str(theword) + guess1[14]
                    elif words.strip()[i] == guess1[15]: #2
                        theword = str(theword) + guess1[15]
                    elif words.strip()[i] == guess1[16]: #3
                        theword = str(theword) + guess1[16]
                    elif words.strip()[i] == guess1[17]: #4
                        theword = str(theword) + guess1[17]
                    elif words.strip()[i] == guess1[18]: #5
                        theword = str(theword) + guess1[18]
                    elif words.strip()[i] == guess1[19]: #6
                        theword = str(theword) + guess1[19]
                    elif words.strip()[i] == guess1[20]: #7
                        theword = str(theword) + guess1[20]
                    elif words.strip()[i] == guess1[21]: #8
                        theword = str(theword) + guess1[21]
                    elif words.strip()[i] == guess1[22]: #9
                        theword = str(theword) + guess1[22]
                    elif words.strip()[i] == guess1[23]: #10
                        theword = str(theword) + guess1[23]
                    elif words.strip()[i] == guess1[24]: #11
                        theword = str(theword) + guess1[24]
                    elif words.strip()[i] == guess1[25]: #12
                        theword = str(theword) + guess1[25]
                    elif words.strip()[i] == guess1[26]: #13
                        theword = str(theword) + guess1[26]
                    else:
                        theword = str(theword)+ "-"
                        
                    #have a word check to see if a word has been completed and
                    #if it matches the requirments.
            
                finished = 0

                #while True:
                comb_check = 0
                #print(theword)
                for i in comb_word[0:int(counter2) + 1] :
                    if theword == i:
                        comb_check = 1

##                try:
##                    if Round == 0:
##                        if theword == comb_word[1]:
##                            Words_left += 1
##                except:
##                    if theword == comb_word[2]:
##                        Words_left += 1
                    
     
                if comb_check == 0 :
                    #----------------------------------------------------------------------------------------------------------
                    #print(words.strip())
                    #this holds the original words being checked in the list.
                    #What must happen is that after the list is used this must clear the list variable and store the new words that fit a certain category into that list.
                    #After this the guesses must be compared to this list instead of the document. aka list is == to words.strip()

                    #-----------------------------------------------------------------------------------------------------------
                    comb_word.insert(int(counter2) + 1, theword)
                    counter2 += 1
                    
                    if Round == 0:
                        if theword == comb_word[1]:
                            lists.insert(int(counts),words)
                            Words_left += 1
                            counts += 1
                            
                    else:
                        if theword == comb_word[2]:
                            lists.insert(int(counts),words)
                            Words_left += 1
                            counts += 1
                        
                    
    #-----------------------------------------------------------
                #If theword matches comb_word[2]
                #in the comb_check list. Add that word to variable list.
                
    #----------------------------------------------------------- 
                    #-----------
                    #add word to list list
                    
                    #If completed word == word in list game over else continue
                    #----------
                    
                for finalwords in theword:
                    if finalwords == "-":
                        finished = 1
                if finished == 0:
                    #--------------------------------------
                    if words in lists[0:200]:
                            #for i in comb_word :
                            #print(i)
                        print(comb_word[-1])
                        #--------------------------------------
                        print("(:(:VICTORY!!!:):)\n \n):How could a person like ypou destroy my perfect programmingness:(")
                        #--------------------------------------
                        gameover = True
                        break

                    #--------------------------------------
                        
                    
            #Have a for loop again so that if it finds a - then the word still
            #needs to be completed BUT if it dosn't find it, it remains 0 and
            #will print you win.

            #Need a way to only look at words that get shown in the option

#guess storage
# no fail safe for if guess has already been entered!!!
    if counter == 0:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 1:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 2:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 3:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 4:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 5:
        guess1[counter + 1] = guess
        counter = counter + 1

    elif counter == 6:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 7:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 8:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 9:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 10:
        guess1[counter + 1] = guess
        counter = counter + 1

    elif counter == 11:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 12:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 13:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 14:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 15:
        guess1[counter + 1] = guess
        counter = counter + 1


    elif counter == 16:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 17:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 18:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 19:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 20:
        guess1[counter + 1] = guess
        counter = counter + 1

    elif counter == 21:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 22:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 23:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 24:
        guess1[counter + 1] = guess
        counter = counter + 1
    elif counter == 25:
        guess1[counter + 1] = guess
        counter = counter + 1 
    elif counter == 26:
        guess1[counter + 1] = guess
        counter = counter + 1     
#------------------------------------------------------------------------

# I need a method where if the list dosn't
#have any words that length it exicutes the statement below


#elif int(len(words.strip())) <= 0:
 #           print("Select a valid Length")
  #          Length = length()
   #         continue


# References 
#Game Settings functions
def length():
    while True:
        try:
            Length = int(input("Enter the word length you wanna play with?"))
            if Length <= 0:
                print("Not valid")
                continue
            else:
                return Length
        except:
            print("Please enter a valid number(no letters) :)")
            continue
    #This is so that if the word length is not a valid number it can be compared to here and rectified.


def nguess():
    #number of guesses
    while True :
        
        try :
            Guesses = int(input("How many guesses do you want?"))
        except :
            print("Please enter a number (not characters)")
            continue

        if Guesses <= 0:
            print("It must Be a number larger than 0  :)")
            continue

        else:
            return Guesses


def start(Letter):
    #letter guess
    while True:
        if gameover == False:
            comb_word = []
            Letter = input("(: Please a enter a letter:")
            Letter = Letter.lower()
            Valid = 0
            for l in "abcdefghijklmnopqrstuvwxyz":
                if l == Letter and Letter not in guess1:
                    return Letter
                else:
                    Valid = 1
            if Valid == 1:
                print("????????????????\nPlease enter a valid letter :)\n????????????????")
                continue
        else:
            return Game
            
    
#must have a way so that it knows if the character is not what is required


#--------------------------------------------------------------------------  
while True:
    comb_word = ["", ""]
    if gameover == False:
        
        print("Welcome to the word guessing game :)")
        countprint = input("Do you want me to display the number of turns left? Y/N: ").lower()
        if countprint == "y" or countprint == "n":
            True
        else:
            print("not valid :)")
            continue
        words_L = input("Do you want me to display the number of words left? Y/N: ").lower()
        if words_L == "y" or words_L == "n":
            True
        else:
            print("not valid :)")
            continue
        
            
        #Input 
        #Game Settings
        guess1 = [None, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

        Length = length()

        Guesses = nguess()
        OGuesses = Guesses 
        first = 0

        while Guesses > 0: 
            if gameover == False:
                if countprint.lower() == "y" and words_L.lower() == "y": #both are YES 
                    print("Turnes left:",Guesses,"words left:",Words_left)
                    if Round == 1:
                        if Words_left == 0:
                            print("no words")
                            break
                    Words_left = 0
                    if Guesses != OGuesses :
                        #print("List",lists)
                        if Round == 0:
                            print(comb_word[1])
                            Round += 1
                        else:
                            try:
                                print(comb_word[2])
                            except:
                                print(comb_word[1])
                        print(guess1[1:int(counter) + 1])

                    comb_word = [None,None]
                    lists = [None,None]

                elif countprint.lower() == "n" and words_L.lower() == "y": #NO YES
                    print("words left:",Words_left)
                    if Round == 1:
                        if Words_left == 0:
                            print("no words")
                            break
                    Words_left = 0
                    if Guesses != OGuesses :
                        #print("List",lists)
                        if Round == 0:
                            print(comb_word[1])
                            Round += 1
                        else:
                            try:
                                print(comb_word[2])
                            except:
                                print(comb_word[1])
                        print(guess1[1:int(counter) + 1])

                    comb_word = [None,None]
                    lists = [None,None]

                elif countprint.lower() == "y" and words_L.lower() == "n": #YES NO
                    print("Turnes left:",Guesses)
                    if Round == 1:
                        if Words_left == 0:
                            print("no words")
                            break
                    Words_left = 0
                    if Guesses != OGuesses :
                        if Round == 0:
                            print(comb_word[1])
                            Round += 1
                        else:
                            try:
                                print(comb_word[2])
                            except:
                                print(comb_word[1])
                        print(guess1[1:int(counter) + 1])

                    comb_word = [None,None]
                    lists = [None,None]

                else:#NO NO
                    if Round == 1:
                        if Words_left == 0:
                            print("no words")
                            break
                    Words_left = 0
                    if Guesses != OGuesses :
                        if Round == 0:
                            print(comb_word[1])
                            Round += 1
                        else:
                            try:
                                print(comb_word[2])
                            except:
                                print(comb_word[1])
                        print(guess1[1:int(counter) + 1])

                    comb_word = [None,None]
                    lists = [None,None]
    
                guess = start(letter)
                if first == 0:
                    Oguess = guess
                    first = 1
                if guess == 0:
                    continue
                Guesses = Guesses - 1
                call(Length, guess)
            else:
                break
        if Guesses <= 0:
            print("game over man, game over")
            print("The word that you had to guess was: ",lists[2])
        while True:
            again = input("Do you want to play again? Y/N: ")
            if again.lower() == "y":
                counter = 0
                os.system('cls')
                gameover = False
                break
            elif again.lower() == "n":
                print("Bye :)")
                gameover = True
                time.sleep(2)
                sys.exit()
            else:
                print("could you say that again?")
                continue

        
        


