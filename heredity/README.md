# Heredity

## Overview
The **Heredity** problem is part of Project 2 in **CS50's Introduction to Artificial Intelligence with Python**. It implements a Bayesian inference AI to compute the probability that each person in a family has 0, 1, or 2 copies of a mutated gene (e.g., GJB2 causing hearing loss), and whether they exhibit the associated trait, based on observed family data.

## What I Learned and Practiced
- **Bayesian Networks**: Modeled gene inheritance and trait expression as a probabilistic graphical model with conditional dependencies.
- **Joint Probability Calculation**: Computed joint probabilities over all variables using conditional independence and mutation probabilities.
- **Evidence Integration**: Used observed traits (or lack thereof) to update prior gene probabilities via likelihoods.
- **Normalization**: Ensured probability distributions sum to 1 while preserving relative likelihoods.
- **Recursive Family Traversal**: Handled multi-generational families by computing gene probabilities conditionally on parents.

## Purpose
The purpose of the Heredity problem is to apply Bayesian inference to real-world genetic modeling. Given partial observations (e.g., who has the trait), the AI computes full posterior distributions over hidden states (gene counts) for every individual, demonstrating how probabilistic reasoning can uncover hidden biological truths from observable data.

## Explanation
The program, implemented in `[heredity.py](/heredity.py)`, uses three key functions:

**1. `joint_probability(people, one_gene, two_genes, have_trait)`**:
- For each person, computes:
  - **Gene probability**:
    - **No parents**: Use `PROBS["gene"]` priors.
    - **With parents**: Sum over inheritance paths:
      - Parent passes gene (0.5 if 1 copy, 1.0 if 2, 0.0 if 0) ± mutation (`PROBS["mutation"]`).
  - **Trait probability**: Use `PROBS["trait"][gene_count][trait]` lookup.
- Multiplies all individual probabilities → joint probability of the full configuration.

**2. `update(probabilities, one_gene, two_genes, have_trait, p)`**:
- Adds joint probability `p` to the correct bin in each person’s `gene` and `trait` distributions.

**3. `normalize(probabilities)`**:
- For each person and each variable (gene/trait), divides all values by their sum → normalized posterior.

**Main Loop**:
- Enumerates **all possible gene configurations** (0, 1, 2 per person).
- For each, computes joint probability given observed traits.
- Updates running totals.
- Normalizes at end → posterior probabilities.

## Demo
Running `python heredity.py data/family0.csv` outputs:

```text
Harry:
  Gene:
    2: 0.0092
    1: 0.4557
    0: 0.5351
  Trait:
    True: 0.2665
    False: 0.7335
James:
  Gene:
    2: 0.1976
    1: 0.5106
    0: 0.2918
  Trait:
    True: 1.0000
    False: 0.0000
Lily:
  Gene:
    2: 0.0036
    1: 0.0136
    0: 0.9827
  Trait:
    True: 0.0000
    False: 1.0000
```

- **James**: High chance of 1–2 genes, 100% trait → strong evidence.
- **Lily**: Very likely 0 genes, 100% no trait → clean.
- **Harry**: Uncertain gene count, ~27% chance of trait → reflects parental ambiguity.

## How to Run
1. Ensure Python 3.12 is installed.
2. Navigate to the folder:
   ```bash
   cd heredity
   ```
3. Run with a family CSV:
   ```bash
   python heredity.py data/family0.csv
   ```
   Try `family1.csv`, `family2.csv` for different cases.

## Files
- **[heredity.py](/heredity.py)**: Main AI with `joint_probability`, `update`, `normalize`.
- **data/**: CSV files with family structure and trait observations.
- **Output**: Console prints probability distributions.

## Reflections
Heredity was my first deep dive into **probabilistic AI**, and it was transformative. Modeling inheritance as a Bayesian network made complex genetics intuitive: every arrow represents a conditional probability. The challenge of enumerating 3ⁿ configurations (n = people) taught me the power and limits of exact inference. Seeing the AI correctly infer Harry’s risk from his parents’ data felt like real science—turning uncertainty into actionable insight. This project bridged biology and AI, showing how machines can reason like genetic counselors.
