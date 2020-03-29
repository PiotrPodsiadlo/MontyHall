import random

rounds = 0
wins = 0
losses = 0
accuracy = 0
cups = ["Yellow", "Pink", "Grey"]

promptStrategy =" Choose strategy!!! (once you choose, all rounds will be played with the same strategy, in order to change strategy restart program)\n Decide if you want to  to stay with your first choice or you want to change cup after first choice \n 1 - stay with initially chosen cup. \n 2 - change cup when there is a chance\n (press Enter to confirm your choice)"
promptScores =   "_______________________________________________________________________________________________ \n\nSo far played {rounds} rounds. Computer won {wins} times and lost {losses} which gives {accuracy} % accuracy \n_______________________________________________________________________________________________\n"
promptIfCountinue = "do you want to play next round? press \"y\" to play next round or \"n\" to finish, \nuse Enter to confirm"
promptWelcome = "There are three cups: {}, {} and {}. \nNoufal hides paper under one of them"
promptExplainRules = "Now computer will try to guess which one. \nyou choose how many times computer plays this game and later you will be informed how many times computer guessed correctly and how many times computer failed\nIn every round you will be informed:\n1 - under which cup Noufal ACUTUALLY put his paper\n2 - what was computer's first choice (radomly guessed)\n3 - computer's second choice after removing one cup from table\n4 - whether computer finally guessed the right cup"
promptHidingPaper = "\nNoufal stored paper under cup {rightCup}"
promptCpuChoice = "Computer chose cup {cpuChoice}"
promptSecondChance = "Noufal removed cup {c0} from game and gave computer second choice with remaining cups {c1} and {c2}"

def explainGameRules():
    print(promptWelcome.format(cups[0], cups[1], cups[2]))
    print(promptExplainRules)
    input("press enter")

def isChoiceRight(cpuChoice, noufalchoice):
    if cpuChoice != noufalchoice:
        return False
    return True

def showStats():
    stats = promptScores.format(rounds = rounds, wins = wins, losses = losses, accuracy = accuracy)
    return stats

def firstGuess(rightCup):
    cpuChoice = random.randint(0, len(cups)-1)
    cupsFor2ndChoice = []
    removedCup = ""
    print(promptHidingPaper.format(rightCup = cups[rightCup]))
    print(promptCpuChoice.format(cpuChoice = cups[cpuChoice]))
    if isChoiceRight(rightCup, cpuChoice) == True:
        cupsFor2ndChoice = [i for i in cups if (i != cups[cpuChoice])]
        cupsFor2ndChoice.append(cups[cpuChoice])
        removedCup = cupsFor2ndChoice.pop(0)
    else:
        cupsFor2ndChoice = [cups[rightCup], cups[cpuChoice]]
        removedCup = [i for i in cups if i not in cupsFor2ndChoice][0]
    print(promptSecondChance.format(c0 = removedCup, c1 = cupsFor2ndChoice[0], c2 = cupsFor2ndChoice[1]))
    return cupsFor2ndChoice

def updateStats(outcome):
    global wins
    global losses
    global accuracy
    if outcome == True:
        wins += 1
    else:
        losses += 1
    if (wins > 0) and (losses > 0):
        accuracy = round(((wins/rounds)*100))
    elif wins > 0:
        accuracy = 100
    else:
        accuracy = 0

def secondGuessWithoutChanges(firstChoice, rightCup):
    print("Computer decided to stay with cup {cup}\n".format(cup = firstChoice[-1]))
    print("Did computer win? " + str(isChoiceRight(firstChoice[-1], cups[rightCup])))
    return isChoiceRight(firstChoice[-1], cups[rightCup])

def secondGuessWithChanges(firstChoice, rightCup):
    print("Computer decided to cange and choose cup {cup}\n".format(cup = firstChoice[-2]))
    print("Did computer win? " + str(isChoiceRight(firstChoice[-2], cups[rightCup])))
    return isChoiceRight(firstChoice[-2], cups[rightCup])

def playRound(inputStrategy, showPrompts = True):
    global rounds
    rightCup = random.randint(0, len(cups)-1)
    firstChoice = []
    if showPrompts == True:
        print(showStats())
        print(promptIfCountinue)
    inp = input()
    if inp == "y":
        rounds += 1
        firstChoice = firstGuess(rightCup)
        if inputStrategy == "1":
            outcome = secondGuessWithoutChanges(firstChoice, rightCup)
        else:
            outcome = secondGuessWithChanges(firstChoice, rightCup)
        updateStats(outcome)
        playRound(inputStrategy)
    elif inp == "n":
        print(showStats())
        print("\nthanks for playing\n")
    else:
        print("press \"y\" or \"n\"")
        playRound(inputStrategy, False)


#PROGRAM START

explainGameRules()

print(promptStrategy)
while 1 == 1:
    inputStrategy = input()
    if (inputStrategy == "1") or (inputStrategy == "2"):
        playRound(inputStrategy)
        break
    else:
        print(inputStrategy)
        print("CHOOSE 1 OR 2")

