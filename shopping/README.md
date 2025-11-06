# Shopping

## Overview
The **Shopping** problem is part of Project 4 in **CS50's Introduction to Artificial Intelligence with Python**. It builds a **1-nearest neighbor (1-NN) classifier** using scikit-learn to predict whether an online shopper will complete a purchase based on 17 behavioral and contextual features.

## What I Learned and Practiced
- **Supervised Learning**: Applied classification to real-world e-commerce data.
- **k-Nearest Neighbors (k-NN)**: Used `KNeighborsClassifier(n_neighbors=1)` for instance-based learning.
- **Feature Engineering**: Converted categorical and boolean data into numeric format (e.g., `Month → 0-11`, `Weekend → 0/1`).
- **Evaluation Metrics**:
  - **Sensitivity (True Positive Rate)**: % of actual buyers correctly identified.
  - **Specificity (True Negative Rate)**: % of non-buyers correctly identified.
- **Data Preprocessing**: Handled mixed data types (int, float, string) from CSV using `csv` module.

## Purpose
The purpose of the Shopping problem is to apply **machine learning** to predict user intent from behavioral signals. It demonstrates how websites can use historical data to personalize experiences (e.g., show discounts to likely non-buyers), balancing sensitivity and specificity for practical utility.

## Explanation
The program, implemented in `[shopping.py](/shopping.py)`, consists of three main functions:

### 1. `load_data(filename)`
- Reads `shopping.csv` using `csv.DictReader`.
- Converts each row into:
  - **Evidence** (17 numeric features):
    - Durations → `float`
    - Counts → `int`
    - Month → `0` (Jan) to `11` (Dec)
    - `VisitorType` → `1` if "Returning_Visitor", else `0`
    - `Weekend` → `1` if "TRUE", else `0`
  - **Labels** → `1` if "TRUE" (purchase), else `0`
- Returns `(evidence_list, labels_list)`

### 2. `train_model(evidence, labels)`
- Initializes `KNeighborsClassifier(n_neighbors=1)`
- Fits the model on training data
- Returns the trained classifier

### 3. `evaluate(labels, predictions)`
- Computes:
  - **True Positives**, **False Negatives**, **True Negatives**, **False Positives**
  - **Sensitivity** = TP / (TP + FN)
  - **Specificity** = TN / (TN + FP)
- Returns `(sensitivity, specificity)`

## Demo
Running:
```bash
python shopping.py shopping.csv
```

**The Output I got:**
```
Correct: 4095
Incorrect: 837
True Positive Rate: 39.84%
True Negative Rate: 90.93%
```

**Interpretation**:
- The model correctly predicts **90.55%** of non-buyers (high specificity).
- It catches **41.02%** of actual buyers (moderate sensitivity).
- Overall accuracy: ~82.9%, far better than random guessing (~85% "no" baseline).

## How to Run
1. Install scikit-learn:
   ```bash
   pip install scikit-learn
   ```
2. Navigate to the folder:
   ```bash
   cd shopping
   ```
3. Run the predictor:
   ```bash
   python shopping.py shopping.csv
   ```

## Files
- **[shopping.py](/shopping.py)**: Full implementation with data loading, k-NN training, and evaluation.
- **[shopping.csv](/shopping.csv)**: Dataset with 12,330 user sessions and 18 columns.
- **requirements.txt**: Contains `scikit-learn`.

## Reflections
Shopping was my first real taste of **applied machine learning**. Turning messy CSV data into numeric features and watching a simple 1-NN model achieve 41% sensitivity and 90% specificity was eye-opening. It showed how even basic algorithms can extract meaningful patterns from user behavior. The balance between sensitivity and specificity highlighted the real-world trade-offs in predictive systems. This project made AI feel tangible—I could imagine this running on a live e-commerce site, nudging hesitant buyers with a well-timed coupon.
