class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!")

    def aviate(self):
        print("I won the lottery and bought a learjet")


class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None: # Annotation; shows live info when this module is imported.
        # if isinstance(duck, Duck):  # Do not use the 'type()' method; better to check instance.
        #     self.flock.append(duck)
        # self.flock.append(duck)
        fly_method = getattr(duck, 'fly', None) # Best Pythonic way.
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__) + "?")

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing exception handler in migrate") # TODO remove this before
            # except AttributeError:
            except AttributeError as e:
                print('One duck down')
                problem = e
                # raise # prints still all the info for debugging
        if problem:
            raise problem # better way to raise the reason of the problem(info), but still running the whole program.


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
