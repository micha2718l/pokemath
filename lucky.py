import random
import numpy as np


class SweetHoney:
    name = "Sweet Honey"

    def use(self):
        heal = 0
        c = "H"
        i = 0
        while c == "H":
            c = np.random.choice(["H", "T"])
            if c == "H":
                i += 1
                heal += 40
        return np.array([heal, i])


class LuckyIcePop:
    name = "Lucky Ice Pop"

    def use(self):
        heal = 20
        c = "H"
        i = 0
        while c == "H":
            c = np.random.choice(["H", "T"])
            if c == "H":
                heal += 20
                i += 1
        return np.array([heal, i])


cards = [SweetHoney(), LuckyIcePop()]
def display():
    for card in cards:
        n = 10000
        h = np.empty((n, 2))
        for i in range(n):
            c = card.use()
            h[i, 0] = c[0]
            h[i, 1] = c[1]

        print(f"Tried {card.name} {n} times.")
        hs = h[:, 0]
        print(f"Max heal: \t\t\t{hs.max()}")
        print(f"Average heal : \t\t\t{hs.mean()}")
        hF = h[:, 1]
        print(f"Max flip: \t\t{hF.max()}")
        print(f"Average flip : \t\t{hF.mean()}\n")
