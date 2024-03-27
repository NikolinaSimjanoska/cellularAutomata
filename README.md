# Cellular Automata Examples

## Overview
This project consists of two examples of cellular automata: a 1D cellular automaton and a 2D cellular automaton. The 1D cellular automaton includes a simple user interface for inputting rules in decimal form, while the 2D cellular automaton is based on Conway's Game of Life.

## 1D Cellular Automaton
The 1D cellular automaton implements a basic user interface allowing users to input rules in decimal form. For reference, you can find a list of rules from 0 to 255 on the [Wolfram website](https://mathworld.wolfram.com/ElementaryCellularAutomaton.html).

### Usage
1. Run the `main.py` script from the 1Dautomat folder.
2. Enter the desired rule in decimal format in the input field.
3. Click the "Start" button to visualize the cellular automaton.

### Dependencies
- Python 3
- Tkinter
- NumPy

## 2D Cellular Automaton (Game of Life)
The 2D cellular automaton is represented using Conway's Game of Life, a classic example of a 2D cellular automaton.

### Conway's Game of Life
Conway's Game of Life operates on a grid of cells, where each cell can be in one of two states: alive or dead. The state of each cell in the next generation is determined by its current state and the states of its eight neighbors.

### Usage
To run Conway's Game of Life:
1. Run the `main.py` script from the 2Dautomat folder.
2. View the initial state of the grid.
3. Click on any cell to toggle its state (alive/dead).
4. The simulation will automatically update according to the rules of the Game of Life.
   
### Dependencies
- Python 3
- NumPy
- Matplotlib

## Additional Information
- The 1D cellular automaton script provides a graphical user interface (GUI) for easy rule input and visualization.
- The 2D cellular automaton script allows user interaction for toggling cell states during simulation.

## Credits
- Conway's Game of Life: [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
