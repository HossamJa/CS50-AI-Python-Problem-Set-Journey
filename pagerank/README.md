# PageRank

## Overview
The **PageRank** problem is part of Project 2 in **CS50's Introduction to Artificial Intelligence with Python**. It implements Google’s PageRank algorithm using **two methods**: (1) **Random Surfer Model** (Monte Carlo sampling) and (2) **Iterative Formula** (convergence). The AI ranks web pages by importance based on link structure, simulating how search engines prioritize results.

## What I Learned and Practiced
- **Markov Chains**: Modeled web navigation as a state transition system with damping factor `d = 0.85`.
- **Monte Carlo Estimation**: Used 10,000 random walks to estimate PageRank via sampling.
- **Iterative Algorithms**: Implemented convergence-based PageRank using the recursive formula until change < 0.001.
- **Damping Factor**: Balanced link-following (85%) vs. random jumps (15%) to prevent trapping in disconnected components.
- **Edge Cases**: Handled pages with no outgoing links by treating them as linking to all pages (including self).

## Purpose
The purpose of the PageRank problem is to understand **probabilistic ranking** in large networks. It introduces **uncertainty modeling** via Markov Chains and demonstrates how **iterative computation** can solve recursive definitions (like PageRank) efficiently. This is foundational to modern search engines and recommendation systems.

## Explanation
The program, implemented in `[pagerank.py](/pagerank.py)`, computes PageRank using two methods:

### 1. **Random Surfer Model (`sample_pagerank`)**
- Start at a random page.
- For `n = 10,000` steps:
  - With probability `d = 0.85`: follow a random outgoing link.
  - With probability `1-d = 0.15`: jump to any page in corpus.
- PageRank = proportion of visits to each page.

### 2. **Iterative Algorithm (`iterate_pagerank`)**
- Initialize: `PR(p) = 1/N` for all pages.
- Repeat until max change < 0.001:
  ```
  PR(p) = (1-d)/N + d * Σ [PR(i) / NumLinks(i)]  for all i → p
  ```
- Pages with no links: treated as linking to all `N` pages.

Both methods converge to similar values, validating correctness.

## Demo
Running `python pagerank.py corpus0` produces:

```text
PageRank Results from Sampling (n = 10000)
  1.html: 0.2223
  2.html: 0.4303
  3.html: 0.2145
  4.html: 0.1329

PageRank Results from Iteration
  1.html: 0.2202
  2.html: 0.4289
  3.html: 0.2202
  4.html: 0.1307
```

**Interpretation**: Page `2.html` is most important (~43%), likely a hub with many incoming links.

## How to Run
1. Ensure Python 3.12 is installed.
2. Navigate to the folder:
   ```bash
   cd pagerank
   ```
3. Run with a corpus directory:
   ```bash
   python pagerank.py corpus0
   ```
   or
   ```bash
   python pagerank.py corpus1
   ```

No external dependencies required.

## Files
- **[pagerank.py](/pagerank.py)**: Main implementation with `transition_model`, `sample_pagerank`, `iterate_pagerank`.
- **corpus0/**, **corpus1/**: Sample web corpora (HTML files + links).
- **Output**: Console prints PageRank from both methods.

## Reflections
PageRank was a brilliant fusion of probability and graph theory. The **random surfer** model made the concept intuitive—importance as visit probability. The **iterative method** showed how recursive definitions become computable through convergence. The damping factor elegantly solved the "trapped surfer" problem. Seeing both methods agree within 0.002 was deeply satisfying. This project revealed how Google revolutionized search with math, not just data.
