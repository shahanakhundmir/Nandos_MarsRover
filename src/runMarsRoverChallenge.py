import sys
sys.path.append('./src')

from marsRover import mars_rover_challenge
from rover import Rover
from plateau import Plateau

print('For the Input: ')
print('Plateau(5,5)')
print("Rover(1, 2, 'N'), directions: LMLMLMLMM ")
print("Rover(3, 3, 'E'), directions: MMRMMRMRRM ")
print('The result is: ')

mars_rover_challenge(Plateau(5,5),[(Rover(1, 2, 'N'),"LMLMLMLMM"),(Rover(3, 3, 'E'),"MMRMMRMRRM")]) 


