######### main.py #########
the main.py script file contains the main game loops that create the main menu, dialogue screen (still working on text animation), and the character selection screen,
which when one of the character icons is selected will load the main game using that character as the player. 

############ Problem ##############
I have managed to figure out the sidescrolling mechanics for my game.
The current isue is FPS, as when I load the game the FPS is around 2. 
I have a feeling that the issue is that the entire map is rendering in the background (outside the viewing window), hence the lag. 
I would like some assistance on how to reduce the lag, and reduce the pixel generation to what is visible inside the viewing window/camera.

############ Files ################
I have uploaded a Level1 folder that contains all the .csv files for the game level 1 terrain loadout + the layers, as well as the level's .tmx file and the desired loadout 
used level1.png 
the main game loop for the generated level of the specific character can be found in chartest.py underneath the section where I have defined the animation frames.
That is where I am trying to add the pygame sidescroller mechanics and physics engine, and am planning to transfer the loop onto a level.py script to increase organisation. 
