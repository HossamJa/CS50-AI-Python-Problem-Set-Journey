# Crossword

## Overview
The **Crossword** problem is part of Project 3 in **CS50's Introduction to Artificial Intelligence with Python**. It generates complete crossword puzzles by solving a **Constraint Satisfaction Problem (CSP)**. Given a grid structure and word list, the AI assigns unique words to each horizontal/vertical sequence such that all overlaps are consistent and all unary constraints (word length) are satisfied.

## What I Learned and Practiced
- **Constraint Satisfaction Problems (CSPs)**: Modeled crossword generation as variables (word slots), domains (words), unary constraints (length), and binary constraints (overlaps).
- **Arc Consistency (AC-3)**: Enforced binary constraints by removing inconsistent values from domains using a queue-based algorithm.
- **Backtracking Search**: Implemented recursive search with forward checking and heuristics.
- **Heuristics**:
  - **Minimum Remaining Values (MRV)**: Selected variable with smallest domain.
  - **Degree Heuristic**: Tiebreaker using number of unassigned neighbors.
  - **Least Constraining Value (LCV)**: Ordered values by how many options they leave for neighbors.
- **Inference**: Used AC-3 during search to prune domains early (optional but implemented for efficiency).

## Purpose
The purpose of the Crossword problem is to apply **optimization via constraint satisfaction** to generate valid puzzles. It demonstrates how AI can solve complex combinatorial problems by combining **consistency enforcement** and **intelligent search**, a technique used in scheduling, planning, and puzzle generation.

## Explanation
The program, implemented in `[generate.py](/generate.py)`, uses the provided `crossword.py` to define the puzzle structure and variables. Key components:

### CSP Components
- **Variables**: Each horizontal/vertical word slot (`Variable(i, j, direction, length)`).
- **Domains**: Initially all words; filtered by length in `enforce_node_consistency`.
- **Constraints**:
  - Unary: Word must match slot length.
  - Binary: Overlapping cells must have same letter.
  - Global: All words must be unique.

### Algorithm Flow
1. **`enforce_node_consistency`**: Remove words with wrong length.
2. **`ac3`**: Enforce arc consistency using a queue of `(x, y)` arcs.
3. **`backtrack`**:
   - Select unassigned variable using **MRV + Degree**.
   - Try values in **LCV** order.
   - Check consistency (length, overlaps, uniqueness).
   - Recursively assign and backtrack on failure.
4. **Output**: Complete assignment → `print()` and `save()` to PNG.

## Demo
Running:
```bash
python generate.py data/structure1.txt data/words1.txt output.png
```

**Console Output**:
```
██████████████
███████M████R█
█INTELLIGENCE█
█N█████N████S█
█F██LOGIC███O█
█E█████M████L█
█R███SEARCH█V█
███████X████E█
██████████████
```

**Generated Image** (`output.png`):
![Crossword Puzzle](output.png)

> Words used: `INTELLIGENCE`, `LOGIC`, `SEARCH`, `SOLVE`, etc. All overlaps consistent and unique.

## How to Run
1. Install Pillow:
   ```bash
   pip install Pillow
   ```
2. Navigate to the folder:
   ```bash
   cd crossword
   ```
3. Generate a puzzle:
   ```bash
   python generate.py data/structure1.txt data/words1.txt output.png
   ```
   (Omit `output.png` to skip image generation.)

## Files
- **[generate.py](/generate.py)**: CSP solver with AC-3, backtracking, and heuristics.
- **[crossword.py](/crossword.py)**: Provided `Variable`, `Crossword` classes.
- **data/**: Structure and word list files.
- **output.png**: Generated puzzle image.

## Reflections
Crossword was the pinnacle of **constraint-driven AI**. The elegance of **AC-3** pruning entire branches before search was transformative. Implementing **MRV + LCV** turned a brute-force explosion into a smooth, efficient solver. Watching a blank grid fill with perfect word fits felt like magic—but it was pure logic. This project showed how AI doesn’t need randomness or learning to solve hard problems: **structure + inference = intelligence**.
