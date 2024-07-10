from random import random
class Trainer:
    def __init__(self, name, team, inventory):
        self.name = name
        self.team = team
        self.inventory = inventory

    def catch_pokemon(self, wild_pokemon, pokeball):
        if pokeball.attempt_catch(wild_pokemon):
            self.team.append(wild_pokemon)
            wild_pokemon.is_wild = False
            print(f'Caught {wild_pokemon.name}!')
        else:
            print(f'{wild_pokemon.name} escaped!')

    def use_item(self, item, target):
        item.use(target)

    def battle(self, opponent):
        while self.team and opponent.team:
            my_pokemon = self.team[0]
            opponent_pokemon = opponent.team[0]

            while my_pokemon.health > 0 and opponent_pokemon.health > 0:
                print(f'{my_pokemon.name} attacks {opponent_pokemon.name}!')
                my_pokemon.attack_opponent(opponent_pokemon, my_pokemon.moves[0])
                
                if opponent_pokemon.health <= 0:
                    print(f'{opponent_pokemon.name} has fainted!')
                    opponent.team.pop(0)
                    my_pokemon.gain_experience(50)
                    break
                
                print(f'{opponent_pokemon.name} attacks {my_pokemon.name}!')
                opponent_pokemon.attack_opponent(my_pokemon, opponent_pokemon.moves[0])
                
                if my_pokemon.health <= 0:
                    print(f'{my_pokemon.name} has fainted!')
                    self.team.pop(0)
                    break
