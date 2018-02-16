import ducks

flock = ducks.Flock()
donald = ducks.Duck()
daisy = ducks.Duck()
duck3 = ducks.Duck()
duck4 = ducks.Duck()
duck5 = ducks.Duck()
duck6 = ducks.Duck()
duck7 = ducks.Duck()
percy = ducks.Penguin()
persian = ducks.Mallard()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(percy) # Not passing if we check the instance.
flock.add_duck(persian)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()
