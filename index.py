import datetime

# Base Class (or parent class) We won't make instances of this directly. IT exists to help us reduce repetition
class Animal:

  def __init__(self, leg_num, species, owner="Happy Acres Breeding Farm"):
    self.owner = owner
    self.species = species
    self.leg_num = leg_num

  def set_solid_food_date(self):
    self.solid_food_date = datetime.datetime.now().strftime("%x")

  def move(self, speed):
    return f"{self.species} moves at {speed} meters per second"


# Derived Class
class Dog(Animal):

  def __init__(self, breed):
    self.breed = breed
    super().__init__(4, "dog")


# Another derived class, also inherits from Animal
class RaceHorse(Animal):

  def __init__(self):
    self.races_won = []
    super().__init__(4, "horse")

  # behavior unique to a horse. Defined here instead of in Animal because our dogs don't run in races
  def add_won_race(self, race):
    self.races_won.append(race)

  # Leverage the general behavior of an Animal moving to create horse-specific moving behaviors
  def trot(self):
    return self.move(8)

  def gallop(self):
    return self.move(15)

# Now we can make some instances!
buttercup = RaceHorse()
buttercup.add_won_race("Preakness")
print(buttercup.races_won)

# make an instance of a Dog
collie = Dog("collie")

# horses and dogs both have leg_nums because it's a property inherited from Animal
print(collie.leg_num)
print(buttercup.leg_num)
# The both have the behavior of setting a solid food date
collie.set_solid_food_date()
buttercup.set_solid_food_date()

# This is a Horse's specific behavior.
print(buttercup.trot())
print(buttercup.gallop())

# A dog can move, because it inherits move(), but it can't trot or gallop
print(collie.move(3))
