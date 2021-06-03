from marsRover import marsRoverChallenge
from rover import Rover
from plateau import Plateau

print('For the Input: ')
print('Plateau(5,5)')
print("Rover(1, 2, 'N'), directions: LMLMLMLMM ")
print("Rover(3, 3, 'E'), directions: MMRMMRMRRM ")
print('The result is: ')

marsRoverChallenge(Plateau(5,5),[(Rover(1, 2, 'N'),"LMLMLMLMM"),(Rover(3, 3, 'E'),"MMRMMRMRRM")]) 


