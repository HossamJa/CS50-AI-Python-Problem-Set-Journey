# Parser

## Overview
The **Parser** problem is part of Project 6 in **CS50's Introduction to Artificial Intelligence with Python**. It implements a **context-free grammar (CFG) parser** using **NLTK** to analyze English sentence structure and extract **noun phrase (NP) chunks**. The AI parses sentences like *"Holmes sat in the little red armchair."* into syntactic trees and identifies base-level noun phrases.

## What I Learned and Practiced
- **Context-Free Grammars (CFGs)**: Designed recursive rules for `S`, `NP`, `VP`, `PP`, etc.
- **Syntactic Parsing**: Converted strings into `nltk.Tree` objects.
- **Tree Traversal**: Used `.subtrees()` to find **leaf-level NPs** (no nested NPs).
- **Tokenization**: Applied `nltk.word_tokenize` + filtering non-alphabetic tokens.
- **Grammar Engineering**: Balanced **coverage** (all sentences parse) vs. **precision** (no overgeneration).

---

## Key CFG Rules (NONTERMINALS)
```python
S  -> NP VP
NP -> Det Adj* N | Det Adj* N PP | N | Pron
VP -> V | V NP | V PP | V NP PP | Adv V
PP -> P NP
Adj* -> Adj Adj* | epsilon
```

**Highlights**:
- `Adj*` allows 0+ adjectives: *"the little red armchair"*
- `PP` enables prepositional phrases: *"in the home"*
- Recursive `NP` supports nesting, but `np_chunk` extracts **only base NPs**

---

## Core Functions

### `preprocess(sentence)`
- Tokenizes using `nltk.word_tokenize`
- Lowercases all words
- Filters out non-alphabetic tokens (e.g., `.`, `28`)
- Returns: `List[str]`

### `np_chunk(tree)`
- Input: `nltk.Tree` with root `S`
- Finds all subtrees where:
  - `.label() == "NP"`
  - No child is an `NP`
- Returns: `List[nltk.Tree]`

---

## Demo
```bash
python parser.py
```

**Input**:
```
Sentence: Holmes sat in the little red armchair.
```

**Parse Tree**:
```
        S
   _____|_____
  NP         VP
  |      _____|____
  N     V         PP
  |     |      ____|____
holmes sat   P         NP
             |      ____|_____
             in   Det   Adj*   N
                  |     |      |
                 the little  red armchair
```

**Noun Phrase Chunks**:
```
holmes
the little red armchair
```

---

## How to Run
1. Install NLTK:
   ```bash
   pip install -r requirements.txt
   ```
2. Navigate to folder:
   ```bash
   cd parser
   ```
3. Run interactively:
   ```bash
   python parser.py
   ```
   → Enter sentences or press Enter to test all in `sentences/`
4. Test a file:
   ```bash
   python parser.py sentences/10.txt
   ```

---

## Files
- **[parser.py](/parser.py)**: Full CFG + preprocessing + NP chunking.
- **sentences/**: 15 test sentences of increasing complexity.
- **requirements.txt**: `nltk`

---

## Grammar Design Notes
| Goal | Strategy |
|------|----------|
| Handle adjectives | `Adj* -> Adj Adj* \| epsilon` |
| Allow PPs in NPs | `NP -> ... \| Det Adj* N PP` |
| Prevent overgeneration | No `Det Det`, no `N N`, no `V V` |
| Parse all 15 sentences | Tested exhaustively |
| Avoid ambiguity explosion | Kept rules minimal but expressive |

**Example Failure Cases (Intentionally Allowed)**:
- `"His Thursday chuckled."` → Parses, but meaningless
- But **not**: `"Armchair on the sat."` → Correctly rejected

---

## Reflections
Parser was **AI meeting linguistics**. Writing a CFG felt like programming in logic — every rule had to be **general yet constrained**. The recursive nature of language became tangible in the parse tree. Extracting **base NPs** via subtree filtering was elegant: no regex, just **structure**. This is how machines will one day *understand* text, not just classify it. **Language is code, and I just compiled it.**
