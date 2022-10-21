import random
name=input("what is your name- ")
print("Best name:",name)
WORD=['RAEHTF','Breake','CYR','Green','aea
roplane']
word=random.choice(WORD)
print("Guess the characters")
guesses=''
turns=5
while turns> 0:
    failed=0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("-")
            print(char,end=" ")
            failed+=1
    if failed==0:
        print("you Win")
        print("The word is :",word)
        break
    print()
    guess=input("guess a character:")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("Worng")
        print("You have",+turns, 'more guesses')
        if turns==0:
            print("You Loose")
        
