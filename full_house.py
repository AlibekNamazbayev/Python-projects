def full_house(hand):
    return all([hand.count(i) >= 2 for i in hand])


print(full_house(["A", "P", "S", "K", "J"]))
