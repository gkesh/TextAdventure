from com.py.entities.gameobject import GameObject


class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.full_health = 3
        self.health = self.full_health
        self._desc = "Name: {}".format(name) + "\n" + "Species: {}".format(
            self.class_name.capitalize()) + "\n" + "Health: ".format(self.health) + "\n" + "A foul creature."
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It was hit on the knee by an arrow."
        elif self.health == 1:
            health_line = "It has a severed limb, the goblin has been jedied."
        elif self.health <= 0:
            health_line = "The goblin is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value
