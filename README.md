# Quantum Checkers

This repository models the behavior of two entangled qubits and their movement through space using the solution to the Schrödinger equation to propogate the wave function. More details can be found in `problem_statement.pdf`.

## Usage

To run the simulation:

    $ python3 simulator.py

Which runs the simulation with default configuration and the default game strategy.

Feel free to edit the current configurations at the bottom of the `simulator.py` file to adjust the size of the map, initial state and starting locations, and more!

Additionally, if you want to test your own strategies, make modifications to the `spin_strategy` method.