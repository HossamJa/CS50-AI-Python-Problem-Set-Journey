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
