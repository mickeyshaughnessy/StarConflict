# Cards subdirectory 
----------
This directory contains all the specific card definitions and data, including
their class attribute and method definitions, ie what they do. 

The `DroneOrbitalDefenders.py` file can be used as a template for new additions.
Note that a new class inherits all the methods attributes from the abstract Card
class in the main directory. Specific cards overwrite these methods and
attributes as needed.

At the end of each card file, the lines following the 

`if __name__ == '__main__':`

line can be used to test the card functionality. Create a game object, 
instantiate the card (or cards if card - card interactions are relevant),
call its methods, and check its attributes and those of the game. 



