import art
import random

def game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    currentcards = {
        "playercards": [],
        "dealercards": [],
    }

    currentcards["playercards"] = [random.choice(cards), random.choice(cards)]
    currentcards["dealercards"] = [random.choice(cards)]

    player_total = sum(currentcards["playercards"])
    dealer_total = sum(currentcards["dealercards"])

    currentcards_player = currentcards["playercards"]
    currentcards_dealer = currentcards["dealercards"]
    print(art.logo)
    print(f"Your cards: {currentcards_player}, current score: {player_total}")
    print(f"Computer's first card: {currentcards_dealer}")

    game_on = True
    while game_on:

        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    #  if player says yes
        if choice == "y":
        # select another random number and add to the player list
            currentcards["playercards"].append(random.choice(cards))
            player_total = sum(currentcards["playercards"])
            print(f"Your cards: {currentcards_player}, current score: {player_total}")
            print(f"Computer's first card: {currentcards_dealer}")
        # calculate if the totals is greater than 21 if not still give a chance to ask the user to hold or pick another card
        # if player goes over 21 dealer wins instantly

            if player_total > 21 and 11 in currentcards["playercards"]:
                currentcards["playercards"].remove(11)
                currentcards["playercards"].append(1)
                player_total = sum(currentcards["playercards"])


            if player_total > 21:
                print(f"Your final hand: {currentcards_player}, final score: {player_total}")
                print(f"Computer's final hand: {currentcards_dealer}, final score: {dealer_total}")
                print("You went over. You lose 😭")
                game_on = False

        else:
            currentcards["dealercards"].append(random.choice(cards))
            dealer_total = sum(currentcards["dealercards"])
            player_total = sum(currentcards["playercards"])

            if dealer_total > 21 and 11 in currentcards["dealercards"]:
                currentcards["dealercards"].remove(11)
                currentcards["dealercards"].append(1)
                dealer_total = sum(currentcards["dealercards"])

            while dealer_total < 17:
                currentcards["dealercards"].append(random.choice(cards))
                dealer_total = sum(currentcards["dealercards"])
                if dealer_total > 21 and 11 in currentcards["dealercards"]:
                    currentcards["dealercards"].remove(11)
                    currentcards["dealercards"].append(1)
                    dealer_total = sum(currentcards["dealercards"])

            if player_total and dealer_total == 21:
                print("It is a draw")
                game_on = False

            if dealer_total > 21:
                print(f"Your final hand: {currentcards_player}, final score: {player_total}")
                print(f"Computer's final hand: {currentcards_dealer}, final score: {dealer_total}")
                print("Your opponent went over, You Win!")
                game_on = False

            else:


                if player_total > dealer_total:
                    print(f"Your final hand: {currentcards_player}, final score: {player_total}")
                    print(f"Computer's final hand: {currentcards_dealer}, final score: {dealer_total}")
                    print("You Win!")
                    game_on = False
                else:
                    print(f"Your final hand: {currentcards_player}, final score: {player_total}")
                    print(f"Computer's final hand: {currentcards_dealer}, final score: {dealer_total}")
                    print("You lose, Dealer Wins")
                    game_on = False


# if hold (no) pick a card for the dealer randomly and add the total >> if the total is less than 17  >> add another random card to dealer card list then calculate total >> if dealer card total >= 17  then you can now compare the total of dealer and player, and the highest close of both wins >> if both are equal to 21, it is a draw.


play_game = True

while play_game:
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if want_to_play == "y":
        game()
    else:
        play_game = False


