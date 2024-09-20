import random

class Pound:
    def __init__(self, rare=False):
        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.color = "gold"
        self.num_edges = 1
        self.diameter = 22.5 # mm
        self.thickness = 3.15 # mm
        self.heads = True


    def rust(self):
        self.color = "greenish"


    def clean(self):
        self.color = "gold"


    def flip(self):
        flip_options = [True, False]
        choice = random.choice(flip_options)
        self.heads = choice


    def __del__(self):
        print("Coin Spent!")


coin1 = Pound()

print(coin1.value)

print(coin1.color)
coin1.color = "greenish"
print(coin1.color)


try:
    pass
except KeyboardInterrupt:
    print("\n[-] Detected CTRL+C ... terminating app, please wait.")

print("\nGoodbye!")
