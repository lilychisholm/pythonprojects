import random


def blackjack():
    def deal_card():
        deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(deck)
        return card

    card1 = deal_card()
    if card1 == 11:
        deck2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card2 = random.choice(deck2)
    else:
        card2 = deal_card()

    card3 = deal_card()
    if card3 == 11:
        deck2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card4 = random.choice(deck2)
    else:
        card4 = deal_card()
    player_hand = [card1, card2]
    player_value = card1 + card2
    computer_hand = [card3, card4]
    computer_value = card3 + card4

    print("Your hand: " + str(player_hand) + ". Your total is " + str(player_value) + '.')
    print("Computer first card: " + str(card3))
    if player_value == 21 and computer_value == 21:
        print("Draw")
    elif player_value == 21:
        print("You won! You got a blackjack :D")
    elif computer_value == 21:
        print("You lost, computer hand was" + str(computer_hand) + ":(")
    else:
        continue_or_not = raw_input("Would you like to draw another card? 'y' or 'n': ")
        while player_value < 21 and continue_or_not == 'y':
            new_card = deal_card()
            player_hand.append(new_card)
            player_value = 0
            for item in range(0, len(player_hand)):
                player_value = player_value + player_hand[item]

            print("You drew " + str(new_card) + ". Your hand:" + str(player_hand) + " Your total: " + str(player_value))
            continue_or_not = raw_input("Would you like to draw another card? 'y' or 'n': ")

        choice = [1, 2]
        computer_draw = random.choice(choice)
        if computer_draw == 1:
            computer_new = deal_card()
            computer_hand.append(computer_new)
            computer_value = 0
            for thing in range(0, len(computer_hand)):
                computer_value = computer_value + computer_hand[thing]

        if player_value > 21 and computer_value > 21:
            print("You both lose, both have a hand over 21. Computer hand: " + str(computer_hand))
            print("Your hand: " + str(player_hand))
        elif player_value > 21:
            print("You lose, your hand was above 21 at " + str(player_hand))
        elif computer_value > 21:
            print("You win! Computer hand above 21 at " + str(computer_hand))
            print("Your hand: " + str(player_hand))
        elif player_value == 21 and computer_value == 21:
            print("Draw, you both got 21.")
        elif computer_value == 21:
            print("You lose, computer at 21 with hand of " + str(computer_hand))
            print("Your hand: " + str(player_hand))
        elif player_value == 21:
            print("You win! You got a blackjack! Player hand: " + str(player_hand))
            print("Computer hand: " + str(computer_hand))
        elif player_value < computer_value:
            print("You lost, computer hand was " + str(computer_hand) + ". Computer total was " + str(computer_value))
            print("Your cards were " + str(player_hand) + ". Your total was " + str(player_value))
        elif player_value > computer_value:
            print("Congratulations! You won. Computer hand was " + str(computer_value))
        else:
            print("Draw")


start_input = raw_input("Would you like to play a game of BlackJack? Enter 'y' or 'n': ")
if start_input == 'y':
    print("Welcome to BlackJack!")
    blackjack()
