class Horce():
    def __init__(self, name, bleed, jockey):
        self.name = name
        self.bleed =bleed
        self.jockey = jockey


class Rider():
    def __init__(self, name):
        self.name = name


the_rider = Rider("Mick Jagger")
stan_the_horse = Horce("Stanley", "friesian", the_rider)


print("The name of Horse is {}".format(stan_the_horse.name))
print("The name of Rides is {}".format(stan_the_horse.jockey.name))

