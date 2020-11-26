class IceCream:
    def __init__(self,flavor,sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles

    @staticmethod
    def sweetest_icecream(lst):
        flavor_values = {
            'Plain':0,
            'Vanilla':5,
            'ChocolateChip':5,
            'Strawberry':10,
            'Chocolate':10
        }
        return max([icecream.sprinkles + flavor_values[icecream.flavor] for icecream in lst])
ice1 = IceCream("Plain",13)
ice2 = IceCream("Plain",0)

print(IceCream.sweetest_icecream([ice1,ice2]))