# Degrees

## Overview
The **Degrees** problem is part of Project 0 in **CS50’s Introduction to Artificial Intelligence with Python**. It implements a program to find the shortest path between two actors based on movies they’ve starred in together, inspired by the "Six Degrees of Kevin Bacon" game. The solution uses breadth-first search (BFS) to compute the minimum degrees of separation.

## What I Learned and Practiced
- **Graph Search Algorithms**: Implemented BFS to find the shortest path in a graph where nodes are actors and edges are movies connecting them.
- **Data Structures**: Worked with dictionaries and sets to store and query people, movies, and their relationships from CSV files.
- **Python Programming**: Used Python 3.12 features, including file I/O, user input handling, and modular function design.
- **Problem Framing**: Learned to model a real-world problem (actor connections) as a graph search problem, understanding states (actors), actions (movies), and goals (target actor).
- **Algorithm Optimization**: Practiced checking for the goal state when adding nodes to the frontier to improve efficiency, as suggested in the problem hints.

## Purpose
The purpose of the Degrees problem is to apply search algorithms to find the shortest path between two actors in a movie database. It simulates the "Six Degrees of Kevin Bacon" game, where any actor can be connected to another within six steps via shared movies. This introduces graph-based search techniques, specifically BFS, to ensure the shortest path is found efficiently.

## Explanation
The program, implemented in `[degrees.py](/degrees.py)`, loads data from three CSV files:
- `people.csv`: Maps actor IDs to names and birth years.
- `movies.csv`: Maps movie IDs to titles and release years.
- `stars.csv`: Links actors to movies they starred in.

The `main` function:
1. Loads data into dictionaries (`names`, `people`, `movies`) using `load_data`.
2. Prompts the user for two actor names, resolving ambiguities with `person_id_for_name`.
3. Calls `shortest_path` to find the shortest sequence of movies connecting the actors.
4. Prints the path, showing each movie and the actors it connects.

The `shortest_path` function, which I implemented, uses BFS:
- **State**: Each node is a `(person_id, path)` tuple, where `path` is a list of `(movie_id, person_id)` tuples leading to the current actor.
- **Frontier**: A queue of nodes to explore, implemented using `QueueFrontier` from `util.py`.
- **Action**: For each actor, explore their co-stars via the `neighbors_for_person` function, which returns `(movie_id, person_id)` pairs.
- **Goal Test**: Check if the current actor is the target; if so, return the path.
- **Optimization**: Check for the target when adding neighbors to the frontier, avoiding unnecessary queue operations.

The algorithm ensures the shortest path by exploring all nodes at the current depth before moving to the next, returning `None` if no path exists.

## Demo
Below is an example output using the `large` dataset:

```
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

This shows a path of three movies connecting Emma Watson to Jennifer Lawrence.

## How to Run
1. Ensure Python 3.12 is installed.
2. Navigate to the folder:
   ```bash:disable-run
   cd degrees
   ```
3. Run the script with a dataset directory (`small` or `large`):
   ```bash
   python degrees.py large
   ```
4. Enter two actor names when prompted.

No additional dependencies are required, as the solution uses only Python’s standard library and the provided `util.py`.

## Files
- **[degrees.py](/degrees.py)**: Main program implementing the Degrees solution.
- **[util.py](/util.py)**: Helper file with `Node`, `StackFrontier`, and `QueueFrontier` classes (provided by CS50).
- **small/**: Small dataset for testing.
- **large/**: Larger dataset for realistic scenarios.

## Reflections
This was my first AI problem, and it was exciting to apply BFS to a real-world scenario like connecting actors. I learned how to model relationships as a graph and optimize search efficiency. The challenge of handling large datasets and ambiguous names deepened my understanding of data structures and algorithmic thinking.
