class Move:
    def __init__(self, name, move_type, power, accuracy, category, effect=None):
        self.name = name
        self.type = move_type
        self.power = power
        self.accuracy = accuracy
        self.category = category
        self.effect = effect

    def apply_effect(self, target):
        if self.effect:
            self.effect(target)

class PhysicalMove(Move):
    def __init__(self, name, move_type, power, accuracy, effect=None):
        super().__init__(name, move_type, power, accuracy, 'Physical', effect)

class SpecialMove(Move):
    def __init__(self, name, move_type, power, accuracy, effect=None):
        super().__init__(name, move_type, power, accuracy, 'Special', effect)

class StatusMove(Move):
    def __init__(self, name, move_type, effect):
        super().__init__(name, move_type, 0, 100, 'Status', effect)
