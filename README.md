# Lights Out General Solver
## What all of this means

Lights out is a puzzle game that has a pretty simple premise. You have an NxN grid with lights on/off, and your goal is to turn off all of them. Hence the name. The gameplay is even simpler: you press a cell, and you switch the cell's light, as well as all of its neighbors. 

Now, I get extremely easily obsessed by puzzle games and making them as optimised as possible. This particular puzzle game I found very satisfying as there exist solvers out there that can determine the optimal solution. My solver (at least, currently) just looks for the first available solution. Credit to the iOS game "Lights Out" for inspiring me to do this.

## Usage

The script awaits two inputs: the dimension and the table. The table is defined in terms of 1s and 0s (cells on or off), and the dimension is an integer.

An example of an execution could be:
```
python3 main.py
6
0 0 0 1 0 1
1 1 1 0 0 1
0 1 0 1 0 1
0 1 0 0 0 0 
0 0 0 1 0 0 
1 1 1 1 1 1
```

## Internal working

Pretty simple and **highly** unoptimized. The solver follows the "Chase the lights" method - look for active cells on layer N, and press the corresponding cells on layer N+1 (or N-1, however you want to see that), that is, the layer below. Afterwards, after one run-through, the solver picks a cell to press and do another run through. If no combination of one or two cells produces a solution, the solver turns the board 90 degrees anticlockwise and tries again until a solution is found and the "additional" presses are determined. The output contains the turns and button presses needed before following the "Chase the lights" method manually in your puzzle

## Disclaimer

This removes all the fun of solving the puzzle. I really enjoy optimizing puzzle solutions, and I feel like this can be helpful to determine a solution and compare yours to this one, but please take into account that the point of logic puzzles is to practice creativity and critical thinking.

Get out of the loop and have fun.