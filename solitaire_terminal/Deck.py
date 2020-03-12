import random
from Card import *

""" d - diamond, h - heart , c - club, s - spade """

c = Card()


class Deck:
    def cardSetup(self):
        deck = []
        pyramid = []
        stock = []
        for n in range(1, 53):  # creates the deck
            deck.append(n)
        random.shuffle(deck)
        pyramid = deck[0:28]  # splits the deck into the two main chunks - pyramid and stock
        stock = deck[28:52]
        return pyramid, stock

    def removeCards(self, firstCard, secondCard, pyramid, stock, waste, foundation):
        """ moves cards from pyramid, stock or waste and adds them to foundation """
        for n in range(len(pyramid)):  # checks all three card locations to find the cards to remove
            if pyramid[n] == firstCard or pyramid[n] == secondCard:
                foundation.append(pyramid[n])
                pyramid[n] = "**"  # makes the pyramid empty card placeholder
        if len(stock) > 0:
            if stock[0] == firstCard or stock[0] == secondCard:
                foundation.append(stock[0])
                stock.pop(0)
        if len(waste) > 0:
            if waste[0] == firstCard or waste[0] == secondCard:
                foundation.append(waste[0])
                waste.pop(0)
        return pyramid, stock, waste, foundation

    def refreshCards(self, pyramid, stock, waste):
        """updates card display lists and display"""
        pcard, scard, wcard = pyramid[:], stock[:], waste[:]  # copies the list to seperate lists so that the program lists stay as numbers
        c.numberToCard(pcard)
        c.numberToCard(scard)
        c.numberToCard(wcard)

        #for n in range(20):  # refreshes the screen and displays the pyramid
        print("      ", pcard[0])
        print("     ", pcard[1], pcard[2])
        print("    ", pcard[3], pcard[4], pcard[5])
        print("   ", pcard[6], pcard[7], pcard[8], pcard[9])
        print("  ", pcard[10], pcard[11], pcard[12], pcard[13], pcard[14])
        print(" ", pcard[15], pcard[16], pcard[17], pcard[18], pcard[19], pcard[20])
        print("", pcard[21], pcard[22], pcard[23], pcard[24], pcard[25], pcard[26],
              pcard[27], "     ", "Stock/Waste - ", scard[0], wcard[0])
