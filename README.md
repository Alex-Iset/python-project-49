<a href="https://ru.hexlet.io/">
<p align="center">
    <img src="images/hexlet_logo.png" 
        width="200" 
        height="200">
</p>
</a>


### Hexlet tests, linter and Code Climate status:
[![Actions Status](https://github.com/Alex-Iset/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Alex-Iset/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/3f97b97684258233f288/maintainability)](https://codeclimate.com/github/Alex-Iset/python-project-49/maintainability)


### Tech Stack:
![Static Badge](https://img.shields.io/badge/python-3.12-%2F?style=flat&logo=python&color=yellow)
![Static Badge](https://img.shields.io/badge/poetry-1.8.4-%2F?style=flat&logo=poetry&color=blue)
![Static Badge](https://img.shields.io/badge/pip-24.0-%2F?style=flat&logo=pip&color=%23DCDCDC)
![Static Badge](https://img.shields.io/badge/prompt-0.4.1-%2F?style=flat&logo=prompt&color=%23DCDCDC)


## Table of contents:
### [1. «Mind games»](#игры-разума)
* [Calculator](#калькулятор)
* [Progression](#прогрессия)
* [Determining an even number](#определение-четного-числа)
* [Determining the greatest common divisor](#определение-наибольшего-общего-делителя)
* [Definition of a prime number](#определение-простого-числа)
### [2. Install (Linux)](#установка-linux)
### [3. How to play?](#как-играть)


## «Mind games»:
«Mind games» — a set of five console games based on the principle of popular mobile
brain-boosting applications. Each game asks questions that need to be answered correctly. 
After three correct answers, it is considered that the game is over. 
Incorrect answers end the game and offer to go through it again.

### Calculator
Arithmetic expressions that need to be calculated

Demonstration of the game "Calculator" using the example of the Makefile command:
[![asciicast](https://asciinema.org/a/1NCaFlTasarIPKNcgn3lZstTK.svg)](https://asciinema.org/a/1NCaFlTasarIPKNcgn3lZstTK)

### Progression
Searching for missing numbers in a sequence of numbers

Demonstration of the game "Progression" using the example of the Makefile command:
[![asciicast](https://asciinema.org/a/uER0wJLTaH6GWrqYBowbK1GmB.svg)](https://asciinema.org/a/uER0wJLTaH6GWrqYBowbK1GmB)

### Determining an even number
Demonstration of the game "Determining an even number" using the example of the Makefile command:
[![asciicast](https://asciinema.org/a/T9ql3NprgTcPp517Es8NUBNwv.svg)](https://asciinema.org/a/T9ql3NprgTcPp517Es8NUBNwv)

### Determining the greatest common divisor
Demonstration of the game "Determining the greatest common divisor" using the example of the Makefile command:
[![asciicast](https://asciinema.org/a/7PG7Rrt1LNijJwIUuA1iGGdfC.svg)](https://asciinema.org/a/7PG7Rrt1LNijJwIUuA1iGGdfC)

### Definition of a prime number
Demonstration of the game "Definition of a prime number" using the example of the Makefile command:
[![asciicast](https://asciinema.org/a/nMDVgnj1M6uzn6BfPMODixuFc.svg)](https://asciinema.org/a/nMDVgnj1M6uzn6BfPMODixuFc)


## Install (Linux):
1. Install pipx
```
sudo apt install pipx
```
2. Install Poetry
```
pipx install poetry
```
3. Cloning a repository
```
git clone https://github.com/Alex-Iset/python-project-49.git
```
4. Going to the "python-project-49" directory
```
cd python-project-49
```
5. Initializing the python-package inside the root directory of the project
```
poetry init
```
6. Creating a virtual environment
```
poetry install
```

## How to play?
You can use Poetry scripts to start the game:
```
poetry run brain-calc
poetry run brain-progression
poetry run brain-even
poetry run brain-gcd
poetry run brain-prime
```
or Makefile commands:
```
make brain-calc
make brain-progression
make brain-even
make brain-gcd
make brain-prime
```
There is also an option to launch games by creating a distribution kit and installing it:
```
make build
make package-install
```
Games can now be run with shorter commands:
```
brain-calc
brain-progression
brain-even
brain-gcd
brain-prime
```