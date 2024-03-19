A simple recreation of the DOS game Mice Men.


Setup:

1. Install the latest version of Python
2. Install the pygame Package(https://www.pygame.org/wiki/GettingStarted)
(A simple way to do this in Windows is navigating to your installation of Python, opening the folder in the terminal and executing the following line of code: "py -m pip install -U pygame --user")
3. Download "Cheese_class.py", "Mice.py" and all pngs and put them into one folder
4. Open the folder with the terminal and start the game with the following line: "py -3 ./Cheese_class.py"


Game Rules

The player has to move all his mice to the other end of the game map. The map consists out of several columns of cheese blocks, which have to be moved around to let your mice pass.
The mice will always move forwards, if they are able to. They can walk on top of cheese blocks and other mice. They will fall down through empty spaces.
You can only move columns, that your own mice stand on. If you push a mouse or cheese block through the roof or floor, they will appear on the opposite side.
The first player to move all their mice off screen has won.


Known Issues

If two mice move along the same path during their turn, sometimes one of them will vanish for a moment. This is only a visual error and does not affect the gameplay.

