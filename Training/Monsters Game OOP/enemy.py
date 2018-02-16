import random


# class Enemy:  # Works the same for Python 3
class Enemy(object):  # Better to use like this in Python 3; the only way in Python 2.

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True
        self.starting_points = hit_points

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{0.name}: I lost one life".format(self))
                self.hit_points = self.starting_points
            else:
                print("{0.name} is dead".format(self))
                self.alive = False

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points}".format(self)


class Troll(Enemy):  # This is a subclass that inherits from the Enemy class
    # pass  # Does nothing. For future development or passing without returning error because it is empty.
    def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)  # Old style Python 2
        super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        # super().__init__(name=name, lives=1, hit_points=23)  # Same results

    def grunt(self):
        print("Me {0.name}. {0.name} stomp you!".format(self))


class Vampyre(Enemy):  # This is a subclass that inherits from the Enemy class, with some changes.

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("***** {0.name} dodges *****".format(self))
            return True
        else:
            return False

    # Overriding the Superclass' take_damage method.
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)  # we use again the original behaviour.

class VampyreKing(Vampyre):

    # Both "super" here, call the methods from the Vampyre and not from Enemy.
    def __init__(self, name):
        super().__init__(name)
        self.hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage // 4)  # integer division.
