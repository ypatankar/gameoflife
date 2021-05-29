# Game Of Life
  
## Introduction
  This project aims to replicate the Game Of Life (refer https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
  
## Setup
  A two-dimensional grid has i * j cells, each of which is in one of the two states:
  
  + 1 corresponds to Alive/live cell
  + 0 correspondents to Dead cell
 
  Every cell interacts with its eight neighbors that are horizontal, vertical or diagonally adjacent. 

## Rules 
  At each step in time, the following transitions occur :    
  1. Any live cell with fewer than two live neighbours dies as if caused by under population.  
  2. Any live cell with two or three live neighbours lives on to the next generation.  
  3. Any live cell with more than three live neighbours dies as if by overcrowding.  
  4. Any dead cell with exactly three live neighbours becomes a live cell as if by reproduction.  

## Getting Started
Cloning the repository will get you a copy of the project up and running on your local machine for development and testing purposes. 

- `git@github.com:ypatankar/gameoflife.git`
- `https://github.com/ypatankar/gameoflife.git`

## Contents
`gameoflife.py`
+ Takes a grid as input and performs evolutionary transitions on the cell based on the rules defined in the docstring
+ Contains Grid class and associated game operations.

## Demo for 25x25 grid for 50 generations
![Alt Text](https://github.com/ypatankar/gameoflife/blob/master/GameOfLife_50_gens.gif)

## Prerequisites
* python 3.x
* python module termcolor to view the live cells movement in color

## Deployment Steps
1. Execute `gameoflife.py` on command line for best output
