# Minesweeper

## Overview
The **Minesweeper** problem is part of Project 1 in **CS50's Introduction to Artificial Intelligence with Python**. It implements an AI that plays Minesweeper using knowledge representation and logical inference. The AI identifies safe cells and mines based on revealed numbers, avoiding guesses when possible, and plays via a Pygame graphical interface.

## What I Learned and Practiced
- **Knowledge Representation**: Created custom `Sentence` class to represent `{cells} = count` logic, avoiding exponential propositional logic explosion.
- **Logical Inference**: Implemented three inference rules: (1) `{cells} = 0` → all safe, (2) `|cells| = count` → all mines, (3) subset inference `{set2-set1} = count2-count1`.
- **Object-Oriented Programming**: Extended `Sentence` and `MinesweeperAI` classes with methods for dynamic knowledge updates and move selection.
- **Set Operations**: Used Python sets for efficient cell tracking, sentence updates, and neighbor calculations.
- **Iterative Inference**: Built a loop that repeatedly applies inferences until no new knowledge is gained, simulating human deduction.

## Purpose
The purpose of the Minesweeper problem is to apply knowledge-based AI to solve a logic puzzle game. Instead of exhaustive model checking (infeasible for 64+ variables), the AI uses compact sentence representations and targeted inference rules to deduce safe moves and mine locations efficiently, demonstrating practical knowledge representation for real-world problems.

## Explanation
The program, implemented in `[minesweeper.py](/minesweeper.py)`, consists of two key classes:

**Sentence Class** (represents `{cells} = count`):
- `known_mines()`: Returns mines if `count == len(cells)` (all cells are mines).
- `known_safes()`: Returns safes if `count == 0` (no mines).
- `mark_mine(cell)`: Removes `cell` from `cells`, decreases `count` by 1.
- `mark_safe(cell)`: Removes `cell` from `cells` (safe cell contributes 0 to count).

**MinesweeperAI Class**:
- `add_knowledge(cell, count)`: 
  1. Marks `cell` as safe/move made.
  2. Creates sentence `{neighbors} = count` (only unknown cells).
  3. **Inference Loop**: Repeatedly applies `known_mines()`, `known_safes()`, and **subset inference** until no new knowledge.
  4. Subset inference: For sentences `S1 = C1`, `S2 = C2` where `S1 ⊆ S2`, add `S2-S1 = C2-C1`.
- `make_safe_move()`: Returns any known safe cell not yet moved.
- `make_random_move()`: Returns random unknown cell (not mine/moved).

The provided `runner.py` handles Pygame GUI, board generation, and AI vs. manual play. The AI prioritizes safe moves, falling back to random only when stuck.

## Demo
Running `python runner.py` launches a graphical Minesweeper game. Click **"AI Move"** to see the AI play:

**Sample AI Session** (9x9 board):
```
[Start: Empty board]
AI Move 1: Clicks center (4,4) → reveals "3"
  Sentence added: {(3,3),(3,4),(3,5),(4,3),(4,5),(5,3),(5,4),(5,5)} = 3
  No immediate inferences.

AI Move 2: Clicks (0,0) → reveals "0"  
  Sentence: {(0,1),(1,0),(1,1)} = 0 → All SAFE!
  AI marks (0,1),(1,0),(1,1) safe → Auto-clicks them.

AI Move 3: Clicks (8,8) → reveals "1"
  Sentence: {(7,7),(7,8),(8,7)} = 1
  Later inference: If {7,7,7,8,8,7} = 2 and above = 1 → {7,7} = 1 → Mine!

[AI flags mine at (7,7)]
[Game continues until win or random guess needed]
```

**Console Output** (when AI moves):
```
Making safe move at (0, 1)
Making safe move at (1, 0)
Making random move at (2, 3)
```

## How to Run
1. Ensure Python 3.12 and Pygame are installed:
   ```bash
   pip install -r requirements.txt
   ```
2. Navigate to the folder:
   ```bash
   cd minesweeper
   ```
3. Run the graphical game:
   ```bash
   python runner.py
   ```
4. Click **"AI Move"** to watch AI play, or click cells manually.

## Files
- **[minesweeper.py](/minesweeper.py)**: AI logic with `Sentence` and `MinesweeperAI` classes.
- **[runner.py](/runner.py)**: Provided Pygame GUI and game engine.
- **[requirements.txt](/requirements.txt)**: Lists `pygame` dependency.

## Reflections
Minesweeper was a breakthrough in understanding practical AI. The `Sentence` representation elegantly solved the propositional logic explosion problem—64 variables became manageable sentences. The subset inference was mind-blowing: simple set operations revealed complex deductions automatically. Watching my AI methodically flag mines and chain safe moves felt like true intelligence emerging from code. This problem showed me how AI can scale logical reasoning to real games, bridging theory and practice beautifully.
