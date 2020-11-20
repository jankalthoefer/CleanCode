# CleanCode - VWmS ESA 

The original TikTakToe from the initial commit was from a previous excercise in Data Science.
I started with that version and improved the code cleaness with every commit.

The changes in each steps are rougly described below.

## Step by step explanation

### Step 1
- File restructuring
- Splitted game logic from user input and output [SoC]

### Step 2
- improved meaning of `player_one:boolean` ==> `current_player: number` variable
- extracted switching players to own method

### Step 3
- improved logic for game state variables
       `win:boolean` ==> `game_over: number`
- seperated "doing" from "calling" code regarding these variables

### Step 4
- seperated player characters (X, O, or whatever character the user could choose from) from the actual game logic. Characters are now handeled by the UI class [SoC]


### Step 5
- general refactoring
- code order now fitting better to the game logic
- added comments for better understanding of each function
