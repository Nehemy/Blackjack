import art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def sum_scores(card_numbers):
    card_sum = sum(card_numbers)
    if card_sum == 21 and 11 in card_numbers and len(card_numbers) == 2:
        return 0
    if card_sum > 21 and 11 in card_numbers:
        card_numbers.remove(11)
        card_numbers.append(1)

    return card_sum

def compare(user_total, dealer_total):
    if user_total == dealer_total:
        return "It is a draw"
    elif dealer_total == 0:
        return "You Lose, opponent has Blackjack"
    elif user_total == 0:
        return "You Win with a Blackjack"
    elif user_total > 21:
        return "You went over. You lose"
    elif dealer_total > 21:
        return "Your opponent went over, You Win!"
    elif user_total > dealer_total:
        return "You win"
    else:
        return "You lose"



def play():
    print(art.logo)
    user_cards = []
    dealer_cards = []
    dealer_cards_total = -1
    user_cards_total = -1


    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    game_on = True
    while game_on:

        user_cards_total = sum_scores(user_cards)
        dealer_cards_total = sum_scores(dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_cards_total}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if user_cards_total == 0 or dealer_cards_total == 0 or user_cards_total > 21:
            game_on = False
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choice == "y":
                user_cards.append(deal_card())
            else:
                game_on = False

        while dealer_cards_total != 0 and dealer_cards_total < 17:
            dealer_cards.append(deal_card())
            dealer_cards_total = sum_scores(dealer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_cards_total}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_cards_total}")
    print(compare(user_cards_total, dealer_cards_total))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play()

