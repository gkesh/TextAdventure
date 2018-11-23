from com.py.entities.gameobject import GameObject
from com.py.entities.goblin import Goblin
from com.py.entities.elf import Elf


class Commands:
    def __init__(self):
        self.verb_dict = {
            "say": self.say,
            "examine": self.examine,
            "hit": self.hit,
            "heal": self.heal,
            "restore": self.restore,
            "create": self.create,
            "exit": self.exit,
        }

        self.class_dict = {
            "goblin": Goblin,
            "elf": Elf,
        }

        self.creatures = {}

    def create(self, noun, name):
        if noun in GameObject.objects:
            msg = "A {} already exists.".format(noun)
        else:
            try:
                if noun in self.class_dict and name not in self.creatures:
                    species = self.class_dict[noun]
                    self.creatures[name] = species(name)
                else:
                    raise NameError
            except NameError:
                msg = "Creature was not created!"
                return msg
            msg = "{0} named {1} was generated.".format(noun.upper(), name.upper())
        return msg

    @staticmethod
    def hit(name):
        if name in GameObject.objects:
            thing = GameObject.objects[name]
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "The {0} named {1} has been slain!".format(thing.class_name, name)
            else:
                msg = "You just hit the {0}, {1}".format(thing.class_name, name)
        else:
            msg = "There is no {} here.".format(name)
        return msg

    @staticmethod
    def heal(name):
        if name in GameObject.objects:
            thing = GameObject.objects[name]
            if type(thing) == Goblin:
                thing.health = thing.health + 1
                if thing.health >= 3:
                    thing.health = thing.health - 1
                    msg = "The {0} named {1} has been completely healed".format(thing.class_name, name)
                else:
                    msg = "You just healed the {0}, {1}".format(thing.class_name,
                                                                name) + "\n" + "Current Health = {}".format(
                        thing.health)
            elif type(thing) == Elf:
                thing.health = thing.health + 1
                if thing.health >= 5:
                    thing.health = thing.health - 1
                    msg = "The {0} named {1} has been completely healed".format(thing.class_name, name)
                else:
                    msg = "You just healed the {0}, {1}".format(thing.class_name,
                                                                name) + "\n" + "Current Health = {}".format(
                        thing.health)
        else:
            msg = "There is no {} here.".format(name)
        return msg

    @staticmethod
    def restore(name):
        if name in GameObject.objects:
            thing = GameObject.objects[name]
            if thing.health == thing.full_health:
                msg = "The {0} named {1} is already completely healthy".format(thing.class_name, name)
            else:
                thing.health = thing.full_health
                msg = "The {0} named {1} has been restored to its full health".format(thing.class_name, name) + "\n" + "Current Health = {}".format(
                    thing.health)
            return msg

    @staticmethod
    def examine(name):
        if name in GameObject.objects:
            return GameObject.objects[name].get_desc()
        else:
            return "There is no {} here.".format(name)

    def get_input(self):
        command = input("-->").split(" ")
        verb_word = command[0].lower()
        if verb_word in self.verb_dict:
            verb = self.verb_dict[verb_word]
        else:
            print("Unknown command {}".format(verb_word))
            return False
        if len(command) == 2:
            name = command[1]
            print(verb(name))
        elif len(command) >= 3:
            noun_word = command[1]
            name = command[2]
            print(verb(noun_word, name))
        else:
            if verb_word == "say":
                print(verb("nothing"))
            else:
                return verb()
        return True

    @staticmethod
    def say(noun):
        return 'You said "{}"'.format(noun)

    @staticmethod
    def exit():
        return False
