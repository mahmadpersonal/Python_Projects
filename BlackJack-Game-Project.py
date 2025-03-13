from art import logo
import random
print(logo)

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  #1st-10 is king and seocnd is queen and third is jack and last is ace=11, 1

def random_card():
    return random.choice(deck)


dealer = {"Card_1": random_card(),
          "Card_2": random_card()
      }
player = {"Card_1": random_card(),
          "Card_2": random_card()
      }

print(f"Dealer Cards: {list(dealer.values())}")
print(f"Player Cards: {list(player.values())}")


def adjust_ace(hand):
    while sum(hand.values()) > 21 and 11 in hand.values():
        for key in hand:
            if hand[key] == 11:
                hand[key] = 1
                break  # Only reduce one Ace at a time
    return sum(hand.values())


dealer_key = 3
while adjust_ace(dealer) < 17:
    dealer[f"Card_{dealer_key}"] = random_card()
    dealer_key += 1

player_key = 3
while adjust_ace(player) < 21:
    hit = input("Press 'h' to hit or 's' to stay: ").lower()
    if hit == "h":
        player[f"Card_{player_key}"] = random_card()
        print(f"Player Cards: {list(player.values())}")
    elif hit == "s":
        break
    else:
        print("Invalid input, please press 'h' or 's'.")
    player_key += 1


dealer_total = adjust_ace(dealer)
player_total = adjust_ace(player)

print(f"\nFinal Dealer Hand: {list(dealer.values())} (Total: {dealer_total})")
print(f"Final Player Hand: {list(player.values())} (Total: {player_total})")

if player_total > 21:
    print("Player Busted! Dealer Wins!")
elif dealer_total > 21:
    print("Dealer Busted! Player Wins!")
elif dealer_total > player_total:
    print("Dealer Wins!")
elif player_total > dealer_total:
    print("Player Wins!")
else:
    print("Push (Tie)!")
