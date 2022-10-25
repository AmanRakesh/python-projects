import random



#Constants
creator = "Amuyo"
LIVES = 3
COMMENT_FOR_GREATER_THAN = "The number is greater than: {number}"
COMMENT_FOR_LESSER_THAN = "The number is lesser than: {number}"
COMMENT_FOR_DIVISIBLE_BY = "The number is divisible by: {number}"
COMMENT_FOR_EVEN_OR_ODD = "The number is: {number}"
EVEN = "EVEN"
ODD = "ODD"
WIN_MESSAGE = "CONGRATS, YOU HAVE WON THE GAME..!!!"
PLAY_AGAIN = "WANNA PLAY AGAIN ??\nPress 1: To play the game again\n2. End the game\nYour input: "
WRONG_GUESS = "oops, your guess was incorrect, try again"
LIVES_LEFT = "you have {lives} lives left"
LIVES_EXHAUSTED = "Sorry but you've exhausted all your lives, so you've lost the game, but you can retry\nGood Luck..!!"
THANKS_FOR_PLAYING = "THANKS FOR PLAYING, SEE YOU AGAIN..!!"
READY_TO_PLAY = "READY, lets start the game...!!!"
RANGE_FOR_GAME = "Enter the number for which the range of the game will be: "
START_RANGE = "the range of the number will start from 0 "
YOUR_GUESS = "now lets take your guess: "
GAME_FINISHED = "your game has finished, the number was: {number}\n\n"


#get factors of the number
def getFactorsOfNumber(num):
    factors = list()
    for i in range(2, num+1):
        if num % i == 0:
            factors.append(i)

    return factors

def getNumberLessThanX(xNum, range):
    if xNum == range:
        return COMMENT_FOR_LESSER_THAN.format(number=xNum)
    return  COMMENT_FOR_LESSER_THAN.format(number=random.randint(xNum + 1, range)) 

def getNumberGreaterThanX(xNum):
    return COMMENT_FOR_GREATER_THAN.format(number=random.randint(0, xNum-1))

def checkNumIsEvenOrOdd(num):
    if num % 2 == 0:
        return COMMENT_FOR_EVEN_OR_ODD.format(number=EVEN)
    else:
        return COMMENT_FOR_EVEN_OR_ODD.format(number=ODD)

def getHint(x, range):
    hint = random.randint(1, 4)
    match hint:
        case 1:
           return checkNumIsEvenOrOdd(x)

        case 2:
            return getNumberLessThanX(x, range)

        case 3:
            return getNumberGreaterThanX(x)

        case 4:
            factors = getFactorsOfNumber(x)
            i = random.randint(0, len(factors)-1)
            return COMMENT_FOR_DIVISIBLE_BY.format(number=factors[i])
        case default:
            "sorry, but no hint for you this time...(^_^)"


print(f"Welcome to the Number Guessing game made by yours truly {creator}\n")

while(True):
    won = False
    print(START_RANGE)
    number = int(input(RANGE_FOR_GAME))
    x = random.randint(0, number)
    print(f"Okay so we have picked a number X from range 0 to {number}, and You have 3 chances to get it right")
    print(READY_TO_PLAY)
    print(f"don't worry we will help you, here's your first hint:\n X is {getHint(x, number)}")
    livesInGame = LIVES
    while(livesInGame>0):
        guessedNumber = int(input(YOUR_GUESS))
        if guessedNumber == x:
            print(WIN_MESSAGE)
            won = True
            break
        else:
            livesInGame-=1
            print(WRONG_GUESS)
            if livesInGame>=1:
                print(LIVES_LEFT.format(lives=livesInGame))
            else:
                print(LIVES_EXHAUSTED)
                break
        print(f"here's your next hint: X is {getHint(x, number)}")
        
    print(GAME_FINISHED.format(number=x))

    game = int(input(PLAY_AGAIN))
    if (game==1):
        continue
    else:
        print(THANKS_FOR_PLAYING)
        break

    
