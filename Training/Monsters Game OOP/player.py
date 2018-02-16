class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3  # we add the "_" to make it deliberatly used when immediate access is needed.
        # If we use the same name with a setter, then it will recursively call itself endlessly until
        # the memory overfloads.
        self._level = 1
        self._score = 0

    # This is a Getter
    def _get_lives(self):
        return self._lives

    # This is a Setter
    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    # This is a Getter
    def _get_level(self):
        return self._level

    # This is a Setter
    def _set_level(self, level):
        if level >= 1:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Cannot be less than 1 level")
            self._level = 1
            self._score = 0

    # Check property syntax: getter, setter, deleter (up to 3 methods).
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    # Different way to create and display properties
    @property  # for Setter
    def score(self):
        return self._score

    @score.setter  # for Getter
    def score(self, score):
        self._score = score

    # Special method that Python searches when we try to print an object.
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0.score}".format(self)
