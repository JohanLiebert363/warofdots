# War of Dots

A real-time strategy simulation game created as a project for **LSP 2026 by Petlja**.

War of Dots is a strategic battlefield where players control armies, capture cities, manage territory, and fight for control of the map. The project focuses on simulation logic, path planning, terrain interaction, and multiplayer-style game mechanics.

## Features

*  Dynamic battlefield simulation
*  Troop movement and combat system
*  Cities that produce and support units
*  Different terrain types affecting gameplay
*  Vision and territory systems
*  Strategic path drawing and unit control
*  Client/server architecture for multiplayer gameplay

## Gameplay

Players control their own territory and units while attempting to expand their influence.

Main objectives:

* Capture and defend cities
* Move troops strategically
* Use terrain advantages
* Defeat enemy forces
* Expand your territory

## Terrain

Different terrain types affect movement, vision, and combat:

| Terrain   | Effects                         |
| --------- | ------------------------------- |
| Plains    | Normal movement and combat      |
| Forest    | Reduced movement and visibility |
| Water     | Movement penalties              |
| Hills     | Defensive and vision advantages |
| Mountains | Impassable terrain              |

## Controls

### Mouse

* **Left Click (Hold)**
  Select troops/cities and draw movement paths.



### Keyboard

* **escape**
  
  quit the game


## Installation

Clone the repository:

```bash
git clone https://github.com/JohanLiebert363/warofdots.git
cd warofdots
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the game:

```bash
python main.py
```

*(The exact start command may vary depending on the project structure.)*

## Project Background

This project was developed as part of **LSP 2026**, organized by **Petlja**.

The goal was to create a complete software project while applying programming concepts such as:

* Object-oriented programming
* Game development principles
* Simulation design
* Networking concepts
* Algorithmic problem solving

## Technologies

* Python
* Pygame
* Networking libraries
* Custom game simulation systems

## Future Improvements

Possible future additions:

* Improved AI opponents
* More unit types
* Better balancing
* Additional maps
* Enhanced multiplayer support
* Improved user interface

## Credits

Developed for **LSP 2026 by Petlja**.

Created by **JohanLiebert363**.
