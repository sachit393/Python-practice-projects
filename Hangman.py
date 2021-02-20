from words import wordslist
import random
word=random.choice(wordslist)
n=len(word)
string=[]
for i in range(0,n):
    string.append('|')
print(string)
lives=5
occurence=[]
wrong_guess=[]
def myindex(t,list):
    try:
        x=list.index(t)
        return x
    except:

        return -1

while lives!=0 and myindex('|',string)!=-1:
    guess=input("Enter you Guess ")
    count=0
    for j in range(0,n):

        if word[j]  == guess :
            lives+=1
            occurence.append(j)
            for k in range(0,n):
                for l in range(k,n):
                    if l==j :string[l]=guess
                count = 1

            print(string)
            if myindex('|',string) != -1:
                print(f"YOU ARE LEFT WITH {lives} lives")
                print(f'Your wrong guesses are {wrong_guess}')

    if(count==0):
        lives-=1
        wrong_guess.append(guess)

        print(f"YOU ARE LEFT WITH {lives} lives")
        print(f'Your wrong guesses are {wrong_guess}')

if(lives==0):
    print("YOU LOSE")
    print(f" THE WORD IS '{ word }'")
else:
    print("YOU WIN")


