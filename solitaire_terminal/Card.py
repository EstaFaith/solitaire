class Card:
    def cardLogic(self, firstCard, secondCard):
        """ compares card selections """
        firstComparison = firstCard
        secondComparison = secondCard
        if firstCard > 13:  # these if and while statements take any card number 1-52 and compares them as 1-13 number
            firstComparison = firstCard - 13
            while firstComparison > 13:
                firstComparison -= 13
        if secondCard > 13:
            secondComparison = secondCard - 13
            while secondComparison > 13:
                secondComparison -= 13
        if firstComparison + secondComparison == 13:  # if the cards add to 13 then the cards can then be moved to the foundation pile
            return "pass"
        else:
            return "fail"

    def stockRotate(self, stock, waste):
        """ simulates card flip from stock to waste pile """

        if len(waste) > 0:
            if waste[0] == "**":  # prevents errors if the waste is just ** as that isn't an integer
                waste.pop()
        if len(stock) != 0:  # adds the top stock card to the top of the waste if the stock isn't empty
            waste.insert(0, stock[0])
        if len(stock) >= 1:
            for n in range(len(stock)-1):  # this removes the stock card that is now on top of the waste pile
                stock[n] = stock[n+1]
            stock.pop()
        else:
            for n in range(len(waste)):  # makes the stock pile the reverse of the waste pile when the stock empties
                stock.insert(0,waste[len(stock)-n])
                waste.pop(0)
            waste = ["**"]   # resets the waste place value
        return stock, waste

    def numberToCard(self, cardsToDisplay):
        """ turns card number of a deck to real cards names """
        cardsToDisplay = cardsToDisplay

        if cardsToDisplay == []:
            cardsToDisplay.append("**")

        for n in range(len(cardsToDisplay)):  # uses numerical values to make unique cards based on the logic that each suit is a multiple of 13 above the last
            if cardsToDisplay[n] != "**":
                suit = "S"
                offset = 39
                if cardsToDisplay[n] <= 39:
                    suit = "C"
                    offset = 26
                    if cardsToDisplay[n] <= 26:
                        suit = "H"
                        offset = 13
                        if cardsToDisplay[n] <= 13:
                            suit = "D"
                            offset = 0
                if cardsToDisplay[n] - offset == 13:  # makes the name - suit cards
                    cardsToDisplay[n] = "K" + suit
                elif cardsToDisplay[n] - offset == 12:
                    cardsToDisplay[n] = "Q" + suit
                elif cardsToDisplay[n] - offset == 11:
                    cardsToDisplay[n] = "J" + suit
                elif cardsToDisplay[n] - offset == 1:
                    cardsToDisplay[n] = "A" + suit
                else:
                    cardsToDisplay[n] = str(cardsToDisplay[n] - offset) + suit  # makes the number - suit cards
        return cardsToDisplay

    def cardToNumber(self, card):
        """ turns a real card back into a number from 1-52 """
        if card[0] == "A":   # does the opposite of the function above basically
            number = 1
        elif card[0] == "J":
            number = 11
        elif card[0] == "Q":
            number = 12
        elif card[0] == "K":
            number = 13
        else:
            number = int(card[0])   # makes the value of the main card then adds it by the suit number
        suitIndex = 1
        if card[1] == "0":
            number = 10
            suitIndex = 2
        if card[suitIndex] == "D":
            suit = 0
        elif card[suitIndex] == "H":
            suit = 13
        elif card[suitIndex] == "C":
            suit = 26
        elif card[suitIndex] == "S":
            suit = 39
        cardNumber = number + suit
        return cardNumber

    def validityCheck(self, card, pyramid, stock, waste, function):
        """checks to see if the card option is valid """
        testPass = "fail"
        rows = [pyramid[0], pyramid[1:3], pyramid[3:6], pyramid[6:10], pyramid[10:15],
                pyramid[15:21], pyramid[21:28]]   # separates the rows of cards into 7 rows
        cardAccess = []
        if len(stock) > 0:  # len(stock) and len(waste) > 0 prevent index errors
            if stock[0] != "**":
                cardAccess.append(stock[0])
        if len(waste) > 0:
            if waste[0] != "**":
                cardAccess.append(waste[0])
        for n in range(len(rows[6])):  # adds the 7th row to the accessible cards if they aren't **
            if rows[6][n] != "**":
                cardAccess.append(rows[6][n])
        for row in range(len(rows) - 1):
            if row != 0:
                for n in range(len(rows[row])):  # adds any other number that has no other cards above it
                    if rows[row + 1][n] == "**" and rows[row + 1][n + 1] == "**":
                        if rows[row][n] != "**":
                            cardAccess.append(rows[row][n])
            else:
                if rows[1][0] == "**" and rows[1][1] == "**":
                    cardAccess.append(rows[0])   # does the final check for the first row access - the for loop above can't check single values, just lists
        for n in range(len(cardAccess)):
            if card == cardAccess[n]:
                testPass = "pass"  # passes available cards from A-Q
                if card % 13 == 0:
                    testPass = "king"  # passes kings and returns a value that lets them skip second card inputs so they are removed straight away
        if function == "cardAccess":  # returns the card access list for the endgame function to use
            return cardAccess
        else:
            return testPass
