# import player
from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing


# Testing for the enemy #######
random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)
print()


# Troll insert ##########
ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

# another_troll = Troll("Ug", 18, 1)  # When we pass in the Troll subclass
another_troll = Troll("Ug")
print("Another troll appears - {}".format(another_troll))

# brother = Troll("Urg", 23)
brother = Troll("Urg")
print(brother)

print()
ugly_troll.grunt()
another_troll.grunt()
brother.grunt()
print()


# Vampyre insert ########
vamp = Vampyre("Vamp")
print("My name is {0.name}. Welcome!".format(vamp))
print(vamp)
vamp.take_damage(10)
print(vamp)

print("-"*40)
another_troll.take_damage(30)
print(another_troll)
vamp.take_damage(20)
print(vamp)

while vamp.alive:
    vamp.take_damage(4)
    print(vamp)


# Vampyre King insert ######
print("-"*40)
dracula = VampyreKing("The Vlad")
print(dracula)
dracula.take_damage(22)
print(dracula)


#########################
# Testing for the player
print()
# tim = player.Player("Tim")
tim = Player("Tim")

print(tim.name)
print("lives: ", tim.lives)

tim.level -= 1
tim.level += 3
print(tim)

tim.lives -= 1
tim.level -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

# tim._lives = 9  # Access directly the object class(deliberatly).
# print(tim)

tim.level = 2
print(tim)
