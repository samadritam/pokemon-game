class EvolutionSys:
    def __init__(self, evolutions):
        self.evolutions = evolutions

    def check_evolution(self, pokemon):
        if pokemon.name in self.evolutions and pokemon.level >= self.evolutions[pokemon.name]['level']:
            evolved_form = self.evolutions[pokemon.name]['evolved_form']
            print(f'{pokemon.name} evolves into {evolved_form}!')
            pokemon.name = evolved_form
            pokemon.level += 1
            pokemon.health += 20
            pokemon.attack += 5
            pokemon.defense += 5
            pokemon.sp_attack += 5
            pokemon.sp_defense += 5
            pokemon.speed += 2
