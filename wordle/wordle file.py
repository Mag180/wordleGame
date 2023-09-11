import random
def Wordgenerator():
    with open("textlol.txt", "r") as wordsFile:
        words = wordsFile.read().split("\n")
    return words[random.randint(0,len(words))]
def wordlist():
    with open("textlol.txt", "r") as wordsFile:
        words = wordsFile.read().split("\n")
    return words



hidden_word = Wordgenerator()
attempts = 5

while (attempts>0):
    guess = input("Guess a five lettered word: ")
    if guess in wordlist():
        if hidden_word == guess:
            print("Congrats!")
            break
        else:
            result = ""
            for i,j in zip(guess, hidden_word):
                if i==j:
                    result = result + (" ✔️ ")
                elif i in hidden_word:
                    result = result + (" ❌ ")
                else:
                    result = result + (" _ ")

            print(result)
            print(f"{attempts-1}  attempts left")
            attempts = attempts - 1
            if attempts == 0:
                print(f"Too bad! The word was {hidden_word} ")
                break
    else:
        print("Word doesn't exist, try again! ")