# Knights

## Overview
The **Knights** problem is part of Project 1 in **CS50's Introduction to Artificial Intelligence with Python**. It solves Raymond Smullyan's classic "Knights and Knaves" logic puzzles using propositional logic and model checking. The program determines whether each character is a knight (always tells truth) or knave (always lies) based on their statements.

## What I Learned and Practiced
- **Propositional Logic**: Encoded complex logical statements using `And`, `Or`, `Not` connectives from `logic.py`.
- **Knowledge Representation**: Modeled puzzles as knowledge bases where sentences represent character statements and their truth conditions.
- **Model Checking**: Used `model_check` to systematically evaluate all possible truth assignments and deduce solutions.
- **Logical Reasoning**: Translated natural language puzzles into concise logical expressions without performing manual reasoning.
- **Constraint Satisfaction**: Encoded mutual exclusivity (each character is exactly one type: knight XOR knave).

## Purpose
The purpose of the Knights problem is to apply propositional logic and model checking to solve logic puzzles automatically. Instead of manually reasoning through contradictions, the AI systematically evaluates all possible scenarios to determine each character's type, demonstrating how knowledge representation enables computers to solve complex logical problems.

## Explanation
The program, implemented in `[puzzle.py](/puzzle.py)`, solves four progressively complex puzzles by constructing knowledge bases:

**Core Structure** (all puzzles):
- `AKnight` ↔ `Not(AKnave)`, `BKnight` ↔ `Not(BKnave)`, etc. (mutual exclusivity)
- Character statements translated into: `IsKnight → Statement` ∧ `IsKnave → Not(Statement)`

**Puzzle 0** (A: "I am both knight and knave"):
```python
knowledge0 = And(
    # A is knight XOR knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # A says "AKnight and AKnave" → false
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)
```

**Puzzle 1** (A: "We are both knaves"):
```python
knowledge1 = And(
    # Mutual exclusivity for A, B
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
    # A says "AKnave and BKnave"
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)
```

**Puzzle 2** (A: "We are same", B: "We are different"):
- Encodes `AKnight ↔ BKnight` and `AKnight ↔ Not(BKnight)` contradictions.

**Puzzle 3** (Complex with uncertainty in A's statement):
- B's meta-statement about what A said requires nested implications.

The `main` function runs `model_check` for each puzzle, printing definitive conclusions (e.g., `A is a knave`).

## Demo
Running `python puzzle.py` produces:

```
Puzzle 0
    A is a Knave
Puzzle 1
    A is a Knave
    B is a Knight
Puzzle 2
    A is a Knave
    B is a Knight
Puzzle 3
    A is a Knight
    B is a Knave
    C is a Knight
    
```

Each puzzle's solution matches manual logical reasoning, confirming the knowledge bases correctly encode the puzzles.

## How to Run
1. Ensure Python 3.12 is installed.
2. Navigate to the folder:
   ```bash
   cd knights
   ```
3. Run the solver:
   ```bash
   python puzzle.py
   ```

No additional dependencies required—uses only `logic.py` (provided).

## Files
- **[puzzle.py](/puzzle.py)**: Main program with knowledge bases for all 4 puzzles.
- **[logic.py](/logic.py)**: Provided library with `And`, `Or`, `Not`, `model_check`.
- **Output**: Console prints solutions for all puzzles.

## Reflections
Solving Knights was a revelation in logical AI. Translating "A says X" into `AKnight → X ∧ AKnave → ¬X` was elegantly simple yet powerful. The model checker handled complex contradictions effortlessly, showing how AI can automate reasoning that would take humans minutes. Puzzle 3's meta-statements were particularly challenging but rewarding. This problem transformed my view of logic from manual puzzle-solving to systematic computation.
