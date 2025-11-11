# Attention

## Overview
The **Attention** problem is the **final challenge** of **CS50's Introduction to Artificial Intelligence with Python**. It uses **BERT** (Bidirectional Encoder Representations from Transformers) via Hugging Face’s `transformers` to:
1. **Predict masked words** in a sentence.
2. **Visualize all 144 self-attention heads** (12 layers × 12 heads) to **interpret what BERT has learned**.

This project bridges **modern NLP** with **AI interpretability** — we don’t just use transformers, we **peek inside them**.

---

## What I Learned and Practiced
- **Masked Language Modeling (MLM)**: BERT’s pretraining objective.
- **Self-Attention Mechanism**: How tokens relate bidirectionally.
- **Hugging Face Transformers**: `TFBertForMaskedLM`, `AutoTokenizer`.
- **Attention Visualization**: Converted attention weights → RGB heatmaps.
- **Interpretability**: Analyzed attention patterns to infer linguistic rules.
- **Tensor Indexing**: Navigated `(layers, batch, heads, seq_len, seq_len)` tensors.

---

## Core Functions

### `get_mask_token_index(mask_token_id, inputs)`
- Returns 0-indexed position of `[MASK]` in token IDs.
- Uses `inputs.input_ids[0]` → list of token IDs.

### `get_color_for_attention_score(score)`
- Maps `[0.0, 1.0]` → `(0,0,0)` to `(255,255,255)` grayscale.
- Linear scaling: `int(round(score * 255))`

### `visualize_attentions(tokens, attentions)`
- Loops over **12 layers × 12 heads = 144**
- For each head: `attentions[layer][0][head]` → attention matrix
- Calls `generate_diagram(layer+1, head+1, ...)`

---

## Demo
```bash
python mask.py
```

**Input**:
```
Text: We turned down a narrow lane and passed through a small [MASK].
```

**Output**:
```
We turned down a narrow lane and passed through a small field.
We turned down a narrow lane and passed through a small clearing.
We turned down a narrow lane and passed through a small park.
```

**Generates 144 PNGs**: `attention_layer_X_head_Y.png`

---

## Attention Head Analysis (`analysis.md`)

> **Head 1: Preposition → Noun (PP Attachment)**  
> **Layer 5, Head 3**  
> This head learns **prepositional phrase structure**. The preposition strongly attends to its **object noun**.  
> - `"We walked [MASK] the bridge."` → `"across"` attends to `"bridge"`  
> - `"The cat slept [MASK] the mat."` → `"on"` attends to `"mat"`  
> → Suggests BERT models **PP attachment** via attention.

> **Head 2: Pronoun → Antecedent (Coreference)**  
> **Layer 8, Head 7**  
> Pronouns attend to their **referents**, even across distance.  
> - `"Alice said she [MASK] tired."` → `"was"` + `"she"` attends to `"Alice"`  
> - `"The doctor helped the patient because he [MASK] caring."` → `"was"` + `"he"` attends to `"doctor"`  
> → BERT tracks **coreference** via long-range attention.

---

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Navigate:
   ```bash
   cd attention
   ```
3. Run:
   ```bash
   python mask.py
   ```
   → Enter text with `[MASK]`

4. **Output**:
   - Top-K predictions
   - 144 attention diagrams in `attention_*.png`

---

## Files
- **[mask.py](/mask.py)**: BERT prediction + 144-head visualization.
- **[analysis.md](/analysis.md)**: Human interpretation of attention patterns.
- **requirements.txt**: `transformers`, `tensorflow`, `matplotlib`, `numpy`

---

## Key Insights from Attention Maps
| Pattern | Layer/Head | Example |
|-------|------------|--------|
| Next-token | L3 H10 | `"then"` → `"i"` |
| Adverb-verb | L4 H11 | `"slowly"` → `"moved"` |
| **PP attachment** | **L5 H3** | `"across"` → `"bridge"` |
| **Coreference** | **L8 H7** | `"she"` → `"Alice"` |

> BERT doesn’t just predict — it **understands syntax and reference**.

---

## Reflections
Attention was the **grand finale**. I didn’t just use BERT — I **opened its mind**. Visualizing 144 attention heads revealed **emergent grammar**: prepositions finding nouns, pronouns tracing back to people. This is how AI learns language — not from rules, but from **relational patterns in data**. The future of NLP isn’t bigger models. It’s **interpretable attention**. I’ve seen the matrix. And it speaks.
