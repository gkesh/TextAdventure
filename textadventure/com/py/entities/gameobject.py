class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc
