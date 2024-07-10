from pokemon import FirePokemon, WaterPokemon
from move import PhysicalMove, SpecialMove
from trainer import Trainer
from pokeball import Pokeball
from evolution import EvolutionSys

# Moves
tackle = PhysicalMove('Tackle', 'Normal', 40, 100)
ember = SpecialMove('Ember', 'Fire', 40, 100)

# Pokémon
charmander = FirePokemon('Charmander', 100, 52, 43, 60, 50, 65, 5, 0, [tackle, ember])
squirtle = WaterPokemon('Squirtle', 110, 48, 65, 50, 64, 43, 5, 0, [tackle])

# Trainers
ash = Trainer('Ash', [charmander], [])
misty = Trainer('Misty', [squirtle], [])

# Battle
ash.battle(misty)
