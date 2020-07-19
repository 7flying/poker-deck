# -*- coding: utf-8 -*-

"""
Simulates drawing cars from a poker deck
"""
import random
import datetime
from builtins import input


def show_commands():
    print (""" available commands:
      - d (draw): draws a card from the deck"
      - s (shuffle): shuffles the deck"
      - e (exit): exit"
      - c (count): count the number of cards in the deck"
      - h (help): shows this help"
    """)


def generate_deck():
    random.seed(datetime.datetime.now())
    deck = []
    for suit in range(1, 5):
        for card in range(1, 14):
            deck.append(str(suit) + str(card))
    return deck


def main_loop():
    print(" the deck has been shuffled, d(raw) a card or s(huffle) the deck")
    print("")
    # spades = "\xE2\x99\xA0"
    # hearts = "\xE2\x99\xA5"
    # diamonds = "\xE2\x99\xA6"
    # clubs = "\xE2\x99\xA3"
    spades = u"\u2660"
    hearts = u"\u2665"
    diamonds = u"\u2666"
    clubs = u"\u2663"
    suits = {'1': spades, '2': hearts, '3': diamonds, '4': clubs}
    deck = generate_deck()
    end = False
    while not end:
        user = input("> ")
        if len(user) != 1:
            continue
        if user == "d":
            card = None
            if len(deck) == 0:
                print("  the deck is empty, reshuffling...")
                deck = generate_deck()
            if len(deck) == 1:
                card = deck.pop(0)
            else:
                # randint both included
                index = random.randint(1, len(deck))
                index -= 1
                card = deck.pop(index)
            if card is None:
                print("SOMETHING WEIRD HAS HAPPENED")
                break
            card_str = card[1:]
            if card_str == "1":
                card_str = "A"
            elif card_str == "11":
                card_str = "J"
            elif card_str == "12":
                card_str = "Q"
            elif card_str == "13":
                card_str = "K"
            print("  " + card_str + suits[card[0]])
        elif user == "s":
            deck = generate_deck()
            print("  the deck has been shuffled")
        elif user == "c":
            print("  the deck has", len(deck), "cards")
        elif user == "h":
            show_commands()
        elif user == "e":
            end = True
        else:
            continue


if __name__ == '__main__':
    print("")
    print(" Welcome to Poker-deck!")
    print ("")
    show_commands()
    main_loop()
