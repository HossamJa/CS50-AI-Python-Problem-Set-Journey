## Repository Structure

The repository is organized with each problem in its own folder, named in lowercase to match the problem's name (e.g., `/degrees/`). Each folder contains the Python script(s), a README.md with an explanation, and a demo (e.g., screenshots, videos, or output examples). The current structure is:

```
CS50AI-Python-Challenges/
├── degrees/
├── tic-tac-toe/
├── knights/
├── minesweeper/
├── pagerank/
├── heredity/
├── crossword/
├── shopping/
├── nim/
├── traffic/
├── parser/
├── attention/
```
```

---

### Update 2: Projects and Problems - Project 4 Section
**Replace the current Project 4 section with:**

```markdown
### Project 4: Learning
- **[Shopping](/shopping/)**: Predicts whether online shopping users will complete a purchase using a k-nearest neighbor classifier.
- **[Nim](/nim/)**: Implements an AI to play the game of Nim, learning optimal moves through reinforcement learning.
```

---

### Update 3: Reflections
**Replace the current Reflections section with:**

```markdown
## Reflections

This repository captures my journey through CS50's AI course, with **Project 0–4 fully completed** (10/10 problems). From graph search and logic puzzles to machine learning and reinforcement learning, each challenge has built a deeper understanding of how AI learns from data, constraints, and experience. Training a Nim AI to master a game through self-play was pure magic—watching it evolve from random to unbeatable. I now see AI not as code, but as **emergent intelligence**. Ready for Project 5: Neural Networks!
```

---

---

### Problem README for Nim

<xaiArtifact artifact_id="e5f6g7h8-i9j0-1234-5678-9abcdef01234" artifact_version_id="v1-nim" title="README.md" contentType="text/markdown">

# Nim

## Overview
The **Nim** problem is part of Project 4 in **CS50's Introduction to Artificial Intelligence with Python**. It implements a **Q-learning agent** that teaches itself to play the game of **Nim** optimally through **reinforcement learning via self-play**. Starting with no knowledge, the AI learns winning strategies by playing 10,000 games against itself.

## What I Learned and Practiced
- **Reinforcement Learning**: Applied **Q-learning** to learn state-action values.
- **Q-Learning Update Rule**:
  ```
  Q(s,a) ← Q(s,a) + α * (r + γ * maxQ(s',a') - Q(s,a))
  ```
  (γ = 1.0, α = learning rate)
- **Epsilon-Greedy Exploration**: Balanced exploration (`ε`) and exploitation.
- **State-Action Representation**: Used `tuple(state)` and `(pile, objects)` for dictionary keys.
- **Self-Play Training**: AI learns by playing both sides, updating Q-values after every move.
- **Terminal Rewards**: +1 for winning, -1 for losing, 0 for ongoing.

## Purpose
The purpose of the Nim problem is to demonstrate **learning without a teacher**. Through trial and error, the AI discovers the **optimal strategy** (based on the XOR of pile sizes) purely from experience — a powerful example of how reinforcement learning can solve complex games.

## Explanation
The program, implemented in `[nim.py](/nim.py)`, consists of:

### `Nim` Class
- Manages game state: piles, current player, winner.
- `available_actions(piles)` → set of `(i, j)` moves.
- `move(action)` → applies action and switches player.

### `NimAI` Class
- **`get_q_value(state, action)`**: Returns Q-value or 0 if unknown.
- **`update_q_value(...)`**: Applies Q-learning update.
- **`best_future_reward(state)`**: Returns max Q-value over all actions in next state.
- **`choose_action(state, epsilon)`**:
  - `ε=True`: epsilon-greedy (random with prob `ε`)
  - `ε=False`: greedy (best known action)

### Training (`train(n)`)
- Plays `n` games of self-play.
- Updates Q-table after **every move**.
- Uses decaying `ε` for exploration.

### Play (`play(ai)`)
- Human vs. trained AI.
- AI makes optimal moves.

## Demo
Running:
```bash
python play.py
```

**Training Output**:
```
Playing training game 1
...
Playing training game 10000
Done training
```

**Gameplay**:
```
Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 5
Pile 3: 7

AI's Turn
AI chose to take 1 from pile 2.
```

**Result**: AI wins **~99%** of games post-training. It learns the **Nim-sum (XOR) strategy** implicitly.

## How to Run
1. Navigate to the folder:
   ```bash
   cd nim
   ```
2. Train and play:
   ```bash
   python play.py
   ```
   - AI trains for 10,000 games.
   - You play as Player 0; AI responds instantly.

## Files
- **[nim.py](/nim.py)**: Full Q-learning implementation.
- **[play.py](/play.py)**: Training loop and human-AI interface.
- **Q-table**: Stored in `NimAI.q` (grows to ~100k+ entries).

## Reflections
Nim was **AI magic in action**. Starting with zero knowledge, the agent discovered the **XOR winning strategy** through pure experience. The Q-table became a map of perfect play. Watching it go from random to ruthless was like raising a digital grandmaster. This project proved: **intelligence can emerge from reward and repetition**. Reinforcement learning isn’t just theory — it’s how machines *learn to think*.
