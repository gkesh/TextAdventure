from com.py.entities.gameobject import GameObject


class Elf(GameObject):
    def __init__(self, name):
        self.class_name = "elf"
        self.full_health = 5
        self.health = self.full_health
        self._desc = "Name: {}".format(name) + "\n" + "Species: {}".format(
            self.class_name.capitalize()) + "\n" + "Health: ".format(self.health) + "\n" + "A beautiful creature."
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 5:
            health_line = "The elf is completely healthy."
            return self._desc + "\n" + health_line
        elif self.health >= 2:
            health_line = "The elf was hit on the arm by a sword."
        elif self.health == 1:
            health_line = "The elf is severly injured."
        elif self.health <= 0:
            health_line = "The elf is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value
