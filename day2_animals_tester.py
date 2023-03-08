#module for testing the package import

#import the package
import animals

#try to make objects from the classes within the package
#harmless animals
harmless_mammals = animals.harmless.Mammals()
harmless_birds = animals.harmless.Birds()
harmless_fish = animals.harmless.Fish()
# dangerous animals
dangerous_mammals = animals.dangerous.Mammals()
dangerous_birds = animals.dangerous.Birds()
dangerous_fish = animals.dangerous.Fish()

#and call functions from them
#harmless animals
harmless_mammals.printMembers()
harmless_birds.printMembers()
harmless_fish.printMembers()
# dangerous animals
dangerous_mammals.printMembers()
dangerous_birds.printMembers()
dangerous_fish.printMembers()
