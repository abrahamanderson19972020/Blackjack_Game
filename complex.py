############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

def is_continue():
    asking= input("Do you want to play again: 'yes' or 'no' >>>")
    if asking.lower() == 'yes':
        global want_continue
        want_continue = True 
    else:
        print("Thanks for playing the game...")
        want_continue = False

print(logo)
print("Blackjack starts...")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
want_continue = True

while want_continue:
    dealer = list()
    player = list()
    for i in range(2):
        dealer.append(random.choice(cards))
        player.append(random.choice(cards))
    print(f"Dealer's card are : {dealer}")
    print(f"Player's cards are : {player}")
    player_want_stand = input("Do you want to hit or stand: write 'hit' or 'stand'>>>")
    if player_want_stand.lower() == "stand":
        dealer_sum = sum(dealer)
        player_sum = sum(player)
        if dealer_sum > 21:
            print("Bust")
            print("Player wins!")
            print(f"Players point is {player_sum}")
            is_continue()
        elif dealer_sum >= 17:
            if dealer_sum > player_sum:
                print("Dealer wins!")
                is_continue()                   
            elif dealer_sum == player_sum:
                print("Draw!")
                is_continue()                  
            else:
                print("Player wins!")
                is_continue()
        else:
            dealer.append(random.choice(cards))
            print(f"Dealer's card are : {dealer}")
            print(f"Player's cards are : {player}")
            dealer_sum = sum(dealer)
            if dealer_sum > 21:
                print("Bust")
                print("Player wins!")
                print(f"Players point is {player_sum}")
                is_continue()
            elif dealer_sum >= 17:
                if dealer_sum > player_sum:
                    print("Dealer wins!")
                    is_continue()
                elif dealer_sum == player_sum:
                    print("Draw!")
                    is_continue()
                else:
                    print("Player wins!")
                    is_continue()
            else:
                dealer.append(random.choice(cards))
                print(f"Dealer's card are : {dealer}")
                print(f"Player's cards are : {player}")
                dealer_sum = sum(dealer)
                if dealer_sum > 21:
                    print("Bust")
                    print("Player wins!")
                    print(f"Player's point is {player_sum}")
                    print(f"Dealer's point is {dealer_sum}")
                    is_continue()
                elif dealer_sum <= 21:
                    if dealer_sum > player_sum:
                        print("Dealer wins!")
                        is_continue()
                elif dealer_sum == player_sum:
                    print("Draw!")
                    is_continue()
                else:
                    print("Player wins!")
                    is_continue()
    else:
        player.append(random.choice(cards))
        print(f"Dealer's card are : {dealer}")
        print(f"Player's cards are : {player}")
        dealer_sum = sum(dealer)
        player_sum = sum(player)
        if dealer_sum > 21:
            print("Bust")
            print("Player wins!")
            print(f"Players point is {player_sum}")
            print(f"Dealers point is {dealer_sum}")
            is_continue()
        elif dealer_sum >= 17:
            if dealer_sum > player_sum:
                print("Dealer wins!")
                is_continue()
            elif dealer_sum == player_sum:
                print("Draw!")
                is_continue()
            else:
                print("Player wins!")
                is_continue()
        else:
            dealer.append(random.choice(cards))
            print(f"Dealer's card are : {dealer}")
            print(f"Player's cards are : {player}")
            dealer_sum = sum(dealer)
            if dealer_sum > 21:
                print("Bust")
                print("Player wins!")
                print(f"Players point is {player_sum}")
                print(f"Dealers point is {dealer_sum}")
                is_continue()
            elif dealer_sum <= 21:
                if dealer_sum > player_sum:
                    print("Dealer wins!")
                    is_continue()
                elif dealer_sum == player_sum:
                    print("Draw!")
                    is_continue()
                else:
                    print("Player wins!")
                    is_continue()


    
