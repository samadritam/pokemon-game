class Pokemon:
    def __init__(self, name, poketype, health, attack, defense, sp_attack, sp_defense, speed, level, experience, moves, is_wild=True):
        self.name = name
        self.type = poketype
        self.health = health
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.level = level
        self.experience = experience
        self.moves = moves
        self.is_wild = is_wild

    def attack_opponent(self, opponent, move):
        damage = self.calculate_damage(opponent, move)
        print(f'{self.name} uses {move.name}! Damage: {damage}')
        opponent.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.faint()

    def gain_experience(self, exp):
        self.experience += exp
        if self.experience >= self.level_up_threshold():
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 2
        self.defense += 2
        self.sp_attack += 2
        self.sp_defense += 2
        self.speed += 1
        print(f'{self.name} leveled up to level {self.level}!')

    def learn_move(self, move):
        if len(self.moves) < 4:
            self.moves.append(move)
        else:
            print(f'{self.name} cannot learn more than 4 moves.')

    def get_stat(self, stat):
        return getattr(self, stat)

    def calculate_damage(self, opponent, move):
        effectiveness = self.get_effectiveness(move.type, opponent.type)
        damage = ((2 * self.level / 5 + 2) * move.power * (self.attack / opponent.defense) / 50 + 2) * effectiveness
        return damage

    def get_effectiveness(self, move_type, opponent_type):
        effectiveness_chart = {
            ('Fire', 'Grass'): 2,
            ('Water', 'Fire'): 2,
            ('Grass', 'Water'): 2,
        }
        return effectiveness_chart.get((move_type, opponent_type), 1)

    def faint(self):
        print(f'{self.name} has fainted!')

    def level_up_threshold(self):
        return 100 * self.level

class FirePokemon(Pokemon):
    def __init__(self, name, health, attack, defense, sp_attack, sp_defense, speed, level, experience, moves, is_wild=True):
        super().__init__(name, 'Fire', health, attack, defense, sp_attack, sp_defense, speed, level, experience, moves, is_wild)

class WaterPokemon(Pokemon):
    def __init__(self, name, health, attack, defense, sp_attack, sp_defense, speed, level, experience, moves, is_wild=True):
        super().__init__(name, 'Water', health, attack, defense, sp_attack, sp_defense, speed, level, experience, moves, is_wild)
