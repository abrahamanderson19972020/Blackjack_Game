############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

import random
from art import logo
from replit import clear


def deal_card():
    """returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(arr):
        """Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
        It check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1"""
        if sum(arr) == 21 and len(arr) == 2:
            return 0 # represents blackjack
        if sum(arr) > 21 and 11 in arr:
            arr.remove(11)
            arr.append(1)
        return sum(arr)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0 :
        return "Computer wins!"
    elif user_score > 21:
        return "Computer wins!"
    elif user_score == 0:
        return "User wins!"
    elif  computer_score > 21:
        return "User wins!"
    elif computer_score > user_score:
        return "Computer wins!"
    else:
        return "User wins!"
    
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
 
    while not is_game_over:
        user_result = calculate_score(user_cards)
        computer_result = calculate_score(computer_cards)
        print(f"Your cards:{user_cards}, your score: {user_result}")
        print(f"Computer card:{computer_cards[0]}")
        if user_result == 0 or computer_result == 0 or user_result > 21:
            is_game_over = True
        else:
            user_answer = input("Get another card: 'y' or 'n'>>>")
            if user_answer == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_result != 0 and computer_result < 17:
        computer_cards.append(deal_card())
        computer_result = calculate_score(computer_cards)


    print(f"Your final cards:{user_cards}, your final score: {user_result}")
    print(f"Computer's final card:{computer_cards}, computer's final score: {computer_result}")
    print(compare(user_result,computer_result))
play_game()
while input("Do you want to continue: 'y' or 'n'>>>").lower() == "y":
    clear()
    play_game()



