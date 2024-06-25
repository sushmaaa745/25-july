class Rodent:
  """
  A class representing a rodent with basic attributes.
  """

  def __init__(self, species, diet):
    self.species = species
    self.diet = diet

  def gnaw(self):
    print(f"{self.species} gnaws on something with its sharp teeth!")

# Inherit from Rodent to create a specific 'Squirrel' class
class Squirrel(Rodent):
  """
  A subclass of Rodent representing a squirrel with additional attributes.
  """

  def __init__(self, species, color, habitat, preferred_nuts):
    super().__init__(species, "Nuts and seeds")  # Call Rodent constructor
    self.color = color
    self.habitat = habitat
    self.preferred_nuts = preferred_nuts

  def gather_nuts(self):
    print(f"{self.species} squirrel ({self.color}) searches for {self.preferred_nuts} in the {self.habitat}!")

  def climb_tree(self):
    print(f"{self.species} squirrel scurries up a {self.habitat} tree!")

  def communicate(self, sound):
    print(f"{self.species} squirrel chatters: '{sound}'")

# Create objects for different squirrel species
eastern_gray_squirrel = Squirrel("Eastern Gray", "Gray", "Deciduous Forest", "Acorns")
red_squirrel = Squirrel("Red", "Rusty Red", "Coniferous Forest", "Spruce cones")
flying_squirrel = Squirrel("Flying", "Brown", "Mixed Forest", "Hazelnuts")

# Simulate squirrel actions
eastern_gray_squirrel.gather_nuts()
red_squirrel.climb_tree()
flying_squirrel.communicate("Chuck!")

# Define functions for environmental interactions (around 40 lines)
def find_food(squirrel, food_list):
  """
  Simulates a squirrel searching for its preferred food in a list.
  """
  if squirrel.preferred_nuts in food_list:
    print(f"{squirrel.species} found {squirrel.preferred_nuts}!")
  else:
    print(f"{squirrel.species} couldn't find {squirrel.preferred_nuts}, but keeps searching...")

def avoid_predator(squirrel, predator):
  """
  Simulates a basic escape response from a predator.
  """
  if predator == "Hawk":
    print(f"{squirrel.species} scurries up a tree to escape the {predator}!")
  else:
    print(f"{squirrel.species} freezes and stays alert for the {predator}!")

# Simulate environmental interactions
food_pile = ["Acorns", "Berries", "Twigs", "Hazelnuts"]
find_food(eastern_gray_squirrel, food_pile)
avoid_predator(red_squirrel, "Hawk")

# Note: This is a basic example. You can expand by:
# - Adding more squirrel species and behaviors.
# - Implementing population management and interactions.
# - Creating a visual representation using libraries like Pygame.

# New Squirrel Species:
# Add a new Fox Squirrel object
fox_squirrel = Squirrel("Fox", "Rusty orange", "Mixed Forest", "Walnuts")
fox_squirrel.gather_nuts()

#Different Communication Sounds:
eastern_gray_squirrel.communicate("Bark!")  
red_squirrel.communicate("Krree!")

#Alternative food sources
eastern_gray_squirrel.diet = "Nuts, seeds, and fruits"  # Update diet for Eastern Gray Squirrel

def find_alternative_food(squirrel):
  if squirrel.preferred_nuts not in food_pile:
    squirrel.diet = "Insects and fungi (alternate)"
    print(f"{squirrel.species} couldn't find preferred food, resorting to {squirrel.diet}.")
