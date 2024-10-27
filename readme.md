# Blackjack Game

Welcome to the **Blackjack Game**! This Python script is a simple console-based implementation of the classic card game, where you play against the dealer to get as close as possible to 21 without going over.

## Features
- **User vs. Dealer Gameplay**: The game follows typical Blackjack rules, where you and the dealer draw cards and attempt to reach a total value of 21.
- **Dealer Rules**: The dealer must draw until reaching at least 17, but if they go over 21, you automatically win.
- **Blackjack Handling**: If either the player or the dealer gets an Ace and a 10-value card as the initial two cards, they get Blackjack (21 points), resulting in an instant win or loss.
  
## How to Play
1. **Start the Game**: Run the script. The game will prompt you to begin a new game.
2. **User’s Turn**: You’ll start with two cards and see one of the dealer’s cards. You can choose to "hit" (get another card) or "stand" (end your turn).
3. **Dealer’s Turn**: The dealer reveals their cards and follows predefined rules to draw until reaching at least 17.
4. **Winning and Losing**: 
   - You win by getting closer to 21 than the dealer or if the dealer goes over 21.
   - You lose by going over 21 or having a lower total than the dealer.
   - A Blackjack on the initial deal (an Ace and a 10-value card) is an automatic win.

## Code Structure
- **deal_card()**: Draws a random card.
- **sum_scores(card_numbers)**: Sums card values and adjusts for the Ace (11 or 1) if necessary.
- **compare(user_total, dealer_total)**: Compares scores between you and the dealer to determine the game outcome.
- **play()**: The main game logic that handles turns, checks for Blackjack, and manages user choices.

## Requirements
- Python 3.x
- `art` module (for displaying the game logo)

To install the `art` module, run:
```bash
pip install art
```

## How to Run
Run the game in your terminal:
```bash
python blackjack_game.py
```
