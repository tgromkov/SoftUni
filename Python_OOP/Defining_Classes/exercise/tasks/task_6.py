class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

        def pokemon_details():
            return f"{self.name} with health {self.health}"


class Trainer:
    def __init__(self, name):
        self.pokemon = []
        pass

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {self.pokemon} with health {self.health}"

    def release_pokemon(self, pokemon_name):
        pass

    def trainer_data(self):
        pass


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
