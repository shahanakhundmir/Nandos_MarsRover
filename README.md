# Mars Rover Challenge :oncoming_automobile:

## Strategy 👷‍♀️
⭐ Approached task using TDD and OOP

⭐ Plateau object with x & y attributes. And Rover object with x, y and direction attributes.

⭐ Separation of Concerns

    🟣 The Mars Rover and validating it's coordinates
  
    🟣 The Plateau and validating it 
    
    🟣 Rover movements
  
    🟣 Formatting the data for output in specified format
    
⭐ Dividing Areas of Concern into functions and writing a failing unit test for each function. Then coding the solution for that function
   
⭐ Building these functions into the main body of the challenge
 

## Cases to check ✔️
:star: Collision - if the current rover is at the same position that a previous rover mission ended at, then a collision has occured
  Print a message about the collision and abort the mission

:star: Before the rover starts its journey and after each move, check that the rover is still on the plateau
  If not then abort the mission

:star: If initial plateau coordinates are (0,0) an error has occured and the mission cannot continue

:star: Check initital compass direction is N, S, E or W

:star: Check that move is L, R or M 


## Written using Python 🐍

## Exceptions ❎
ValueErrors are generated for:

:star: Invalid Inputs

:star: Invalid Plateau coordinates

:star: If the rover is no longer on the Plateau

:star: Collision between 2 Rovers


## Testing 📑
:star: Tests have been carried out on isolated functions

:star: Thorough testing of edge cases, including collision, valid inputs and the rover remaining on the plateau

:star: Testing checks if missions are aborted and error messages returned

:star: If more than one rover is on a mission, a list of outputs is returned

:star: Output is a Rover object for each rovers final position, with coordinates and compass direction

:star: Error messages are string with Mission aborted and reason why. 

:star: The Rover Missions object format output is converted to String as per the specification and printed to screen


## To Run 🏃‍♂️

📁 git clone https://github.com/shahanakhundmir/Nandos_MarsRover.git

🧪 There are 3 test files, to execute these run the following commands:

pytest test_rover.py / python -m pytest test_rover.py

pytest test_plateau.py  / python -m pytest test_plateau.py

pytest test_challenge.py  / python -m pytest test_challenge.py

:computer: To run the challenge with preloaded input, run the following command:

python runMarsRoverChallenge.py


