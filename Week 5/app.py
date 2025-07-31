# Base Class
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.__level = level  # Encapsulated attribute (private)

    def show_identity(self):
        print(f"I am {self.name}, and my power is {self.power}!")

    def get_level(self):
        return self.__level

    def level_up(self):
        self.__level += 1
        print(f"{self.name} leveled up to {self.__level}!")

# Subclass (Inheritance)
class Avenger(Superhero):
    def __init__(self, name, power, level, weapon):
        super().__init__(name, power, level)
        self.weapon = weapon

    def use_weapon(self):
        print(f"{self.name} uses their weapon: {self.weapon}!")

    # Polymorphism: override show_identity()
    def show_identity(self):
        print(f"Avenger {self.name} with power '{self.power}' wields a {self.weapon}!")

# Create objects
hero1 = Superhero("Flash", "Speed", 5)
hero2 = Avenger("Thor", "Thunder", 8, "Mjolnir")

# Demonstrate functionality
hero1.show_identity()
hero1.level_up()

hero2.show_identity()  # Polymorphism in action
hero2.use_weapon()
print("Thor's level:", hero2.get_level())