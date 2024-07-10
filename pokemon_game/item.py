class Item:
    def __init__(self, name, item_type, effect):
        self.name = name
        self.type = item_type
        self.effect = effect

    def use(self, target):
        self.effect(target)
