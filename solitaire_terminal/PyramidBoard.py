from Deck import *
from Card import *

d = Deck()
c = Card()


class PyramidBoard:
    def errorChecking(self, userInput, inputType):
        """ handles user inputs to prevent errors """
        validCardsValues = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "J", "Q",
                            "K"]  # creating the correct input strings
        validSuits = ["D", "H", "C", "S"]
        if inputType == "menu":
            try:
                int(userInput)  # prevents a value error if the user inputs a letter
            except ValueError:
                print("Use a numerical response")
                return "fail"
            if 0 < int(userInput) <= 3:  # prevents the user from inputting an erroneous menu error
                return "pass"
            else:
                print("Please choose a valid numerical option")
                return "fail"
        elif inputType == "cardChoice":
            length = True
            for n in range(0, 2):
                try:
                    userInput[n]  # prevents the user from inputting an incorrect card name length
                except IndexError:
                    length = False
            if length:
                for n in range(len(validCardsValues)):
                    if userInput[0] == validCardsValues[n]:  # checks to see if the user inputs the right card value
                        suitIndex = 1
                        if userInput[0] == "1":
                            suitIndex = 2
                            try:
                                userInput[2]
                            except IndexError:
                                length = False
                        if length:
                            for n in range(len(validSuits)):
                                if userInput[suitIndex] == validSuits[n]: # checks if the user inputs the right suit names
                                    return "pass"
            print("Invalid card name, try again")
            return "fail"

    def cardSelection(self, pyramid, stock, waste, foundation):
        """ takes card input, validates, compares and removes valid cards """
        validResponse = "fail"
        while validResponse == "fail":
            firstCard = input(
                "Enter the valid card name, or go back (b) : ")  # collects the first card selection from the user
            firstCard = firstCard.upper()
            if firstCard == "B":
                return
            validResponse = self.errorChecking(firstCard, "cardChoice")

        firstCard = c.cardToNumber(firstCard)
        if c.validityCheck(firstCard, pyramid, stock, waste, "check") == "pass":
            validResponse = "fail"
            while validResponse == "fail":
                secondCard = input(
                    "Enter the second valid card to compare, or go back (b) : ")  # collects the second card from the user
                secondCard = secondCard.upper()
                if secondCard == "B":
                    return
                validResponse = self.errorChecking(secondCard, "cardChoice")
            secondCard = c.cardToNumber(secondCard)
            if c.validityCheck(secondCard, pyramid, stock, waste, "check") == "pass":
                if c.cardLogic(firstCard, secondCard) == "pass":
                    pyramid, stock, waste, foundation = d.removeCards(firstCard, secondCard, pyramid, stock, waste,
                                                                      foundation)
        elif c.validityCheck(firstCard, pyramid, stock, waste, "check") == "king":
            pyramid, stock, waste, foundation = d.removeCards(firstCard, "none", pyramid, stock, waste, foundation)

    def endConditions(self, pyramid, stock, waste):
        """checks to see if the game is completed or impossible to complete"""
        if len(stock) > 0:  # sets up values to pass to validityCheck function
            emS = [stock[0]]
        else:
            emS = ["**"]
        if len(waste) > 0:
            emW = [waste[0]]
        else:
            emW = ["**"]
        pyramidAccess = c.validityCheck(0, pyramid, emS, emW,
                                      "cardAccess")  # makes the card access lists for this function
        pyramidAccess = pyramidAccess[
                        2:]  # first two cards in pyramidAccess right now are the top of the stock and waste so they are removed
        cardAccess = c.validityCheck(0, pyramid, emS, emW,
                                   "cardAccess") + stock + waste  # makes a list of all accessible cards in game
        cardsToPop = []
        for n in range(len(cardAccess)):  # removes all of the card placeholders from the list if they exist
            if cardAccess[n] == "**":
                cardsToPop.append(n)
        if len(cardsToPop) > 0:
            for n in range(len(cardsToPop)):
                cardAccess.pop(cardsToPop[n])
        passCounter = 0
        for first in range(2, len(pyramidAccess) + 2):  # checking valid pyramid cards with the stock and waste
            for second in range(len(cardAccess)):
                if c.cardLogic(cardAccess[first], cardAccess[second]) == "pass":
                    passCounter += 1
        swCombinations = stock + waste
        for n in range(len(swCombinations)):
            if swCombinations[n] == "**":
                swCombinations.pop(n)
        for n in range(
                len(swCombinations) - 1):  # checking to see if the stock and waste can make any final combinations
            if c.cardLogic(swCombinations[n], swCombinations[n + 1]) == "pass":
                passCounter += 1
        if passCounter == 0:
            print("There are no more combinations!")
            return "end"  # ends the game when the pyramid has cards left which can't be removed
        for n in range(len(pyramid)):
            if pyramid[n] != "**":
                return "continue"
            else:
                print("Well done! You removed the pyramid!")
                return "end"

    def scoring(self, pyramid, foundation):
        """ tracks the performance of the player """
        rows = [pyramid[0], pyramid[1:3], pyramid[3:6], pyramid[6:10], pyramid[10:15],
                pyramid[15:21], pyramid[21:28]]  # makes the card rows like in validityCheck function
        score = 0
        sortedPyramidCards = 0
        if pyramid[0] == "**":  # adds score if the last pyramid card is removed
            score += 4200
            sortedPyramidCards += 1
        for row in range(1, len(rows)):  # adds score for the rest of the pyramid cards
            for card in range(len(rows[row])):
                scoreAddition = int(2100 / row)
                if rows[row][card] == "**":
                    score = score + scoreAddition
                    sortedPyramidCards += 1
        for n in range(sortedPyramidCards, len(
                foundation)):  # adds score for any extra cards not in the pyramid that removed (from stock/waste)
            score += 300
        print("Your score was: ", score)


def main():
    """ simulate regular program operation """
    p = PyramidBoard()
    print("------- Welcome to the Pyramid Solitaire -------")
    print("Enter:\n 1 - Start\n 2 - Rules\n 3 - Finish game")
    validResponse = "fail"
    choice = input()
    while validResponse == False:
        validResponse = p.errorChecking(choice, "menu")
    choice = int(choice)
    if choice == 2:
        information = open("rules.txt", "r")
        print(information.read())  # prints the rules screen
        input()
    elif choice == 3:
        print("Closing game...")
        return
    endgame = "continue"
    waste = ["**"]
    pyramid, stock = d.cardSetup()
    foundation = []
    while endgame == "continue":
        d.refreshCards(pyramid, stock, waste)
        validResponse = "fail"
        while validResponse == "fail":
            choice = input("Choose: 1 - Card Selection, 2 - Stock Rotation, 3 - End Game. ")
            validResponse = p.errorChecking(choice, "menu")
        choice = int(choice)
        if choice == 1:
            p.cardSelection(pyramid, stock, waste, foundation)
            endgame = p.endConditions(pyramid, stock, waste)
        elif choice == 2:
            stock, waste = c.stockRotate(stock, waste)
            endgame = p.endConditions(pyramid, stock, waste)
        else:
            endgame = "end"
    p.scoring(pyramid, foundation)
    input("Press Enter to end.")


main()
