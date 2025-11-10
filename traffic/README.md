# Traffic

## Overview
The **Traffic** problem is part of Project 5 in **CS50's Introduction to Artificial Intelligence with Python**. It implements a **Convolutional Neural Network (CNN)** using **TensorFlow/Keras** to classify **43 types of German traffic signs** from images in the **GTSRB dataset**. The model achieves **~95.35% test accuracy** after 10 epochs.

## What I Learned and Practiced
- **Deep Learning**: Built and trained a CNN from scratch.
- **Computer Vision**: Preprocessed images using OpenCV (`cv2.imread`, `cv2.resize`).
- **Convolutional Layers**: Used `Conv2D` + `MaxPooling2D` to extract spatial features.
- **Regularization**: Applied `Dropout(0.5)` to prevent overfitting.
- **Data Pipeline**: Loaded, resized, and batched image data with `tf.keras.utils.image_dataset_from_directory`.
- **Model Architecture**: Experimented with depth, filter size, and pooling.
- **Transfer Learning (Bonus)**: Considered but implemented custom CNN for learning.

## Purpose
The purpose of the Traffic problem is to apply **deep learning to real-world perception**. Self-driving cars must recognize traffic signs instantly and accurately. This project shows how **neural networks learn visual patterns** from raw pixels — a core capability of modern AI.

---

## Model Architecture
```python
Input → [Conv2D(32, 3×3) → ReLU → MaxPool] × 2
      → [Conv2D(64, 3×3) → ReLU → MaxPool]
      → Flatten → Dense(128) → Dropout(0.5) → Output(43)
```

**Key Design Choices**:
- **Progressive filters** (32 → 64): Learn simple edges → complex shapes.
- **MaxPooling**: Reduce dimensions, retain important features.
- **Dropout(0.5)**: Prevent overfitting on small dataset.
- **Adam optimizer + Sparse Categorical Crossentropy**: Standard for multi-class.

---

## Training Results
```text
Epoch 10/10
500/500 [==============================] - 10s 20ms/step - loss: 0.2497 - accuracy: 0.9256
333/333 - 5s - loss: 0.1616 - accuracy: 0.9535
```

**Final Test Accuracy: 95.35%**

---

## How to Run

### 1. **Download Test Data**
> **Warning**: The dataset is **~300MB**. Download and extract:
```bash
wget https://cdn.cs50.net/ai/2023/x/projects/5/gtsrb.zip
unzip gtsrb.zip
```

### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```
> Requires: `tensorflow`, `opencv-python`, `scikit-learn`

### 3. **Train & Evaluate**
```bash
cd traffic
python traffic.py gtsrb
```

### 4. **Save Model (Optional)**
```bash
python traffic.py gtsrb my_traffic_model.h5
```

---

## Files
- **[traffic.py](/traffic.py)**: Full CNN implementation with data loading and model training.
- **[gtsrb/](/gtsrb/)**: Dataset with 43 classes (~39k train, ~12k test images).
- **requirements.txt**: Lists `tensorflow`, `opencv-python`, `scikit-learn`.

---

## Experimentation (README.md Requirement)

> **What I Tried**:
> - Shallow CNN (1 conv layer): ~70% accuracy.
> - Deeper CNN (5+ layers): Overfitting, slower convergence.
> - Larger filters (5×5): Worse than 3×3.
> - No dropout: Val accuracy plateaued at ~88%.
> - BatchNorm: Slight improvement but longer training.
> - Data augmentation (`ImageDataGenerator`): Helped but not used in final (kept simple).
>
> **What Worked Best**:
> - **3 Conv + Pool layers** with **32→64 filters**.
> - **Dropout(0.5)** after dense layer.
> - **30×30 input** (balanced speed/accuracy).
> - **Adam + default LR**.
>
> **Key Insight**: CNNs learn hierarchical features, early layers detect edges, later layers detect sign shapes. Dropout was critical due to class imbalance and small dataset.

---

## Reflections
Traffic was my **first deep learning victory**. Watching loss drop from 3.7 to 0.16 and accuracy climb to **95.35%** felt like teaching a machine to *see*. The CNN didn’t just memorize — it learned **invariant patterns** across rotations, lighting, and blur. This is the future of autonomous vehicles, medical imaging, and beyond. **AI doesn’t just compute — it perceives.**
