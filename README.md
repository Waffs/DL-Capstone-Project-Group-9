# Deep Learning-Based Classification of Nigerian Traditional Attire

**Authors:**  
Naziru Abdussalam Ibrahim • Ahmad Saad • Abdulwasiu B. Popoola • Taiwo Soffiyah Abass • Ayodeji Akande • Shamsu Abdullahi • Abubakar Sadiq Sulaiman • Yahya Abdurrazaq

**Published:** June 1, 2025

---

##  Overview

This project applies **Convolutional Neural Networks (CNNs)** to classify images of traditional Nigerian attire by ethnic group. Two prominent architectures—**ResNet-34** and **EfficientNet-B0**—are fine-tuned via transfer learning to create an automated, culturally enriching classification system :contentReference[oaicite:0]{index=0}.

---

## Table of Contents

- [Background](#background)  
- [Data Pipeline](#data-pipeline)  
- [Models & Training](#models--training)  
- [Evaluation](#evaluation)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  

---

## Background

- Nigeria is home to over 250 ethnic groups, each with unique traditional attire reflecting rich cultural identities :contentReference[oaicite:1]{index=1}.
- Manual classification is prone to subjectivity and inefficiency; this model offers a scalable, objective solution.

---

## Data Pipeline

- **Collection:** Used custom Python scripts—`download_attire.py` and `download_attire_extended.py`—to gather images across categories such as Yoruba, Hausa, Igbo, etc. :contentReference[oaicite:2]{index=2}
- **Preprocessing:** Images were resized, normalized, and augmented to improve model generalization. The dataset was split into training, validation, and test sets. :contentReference[oaicite:3]{index=3}

---

## Models & Training

Two CNN architectures were employed:

- **ResNet-34:** A 34-layer residual network; addresses vanishing gradients via skip connections. :contentReference[oaicite:4]{index=4}  
- **EfficientNet-B0:** Lightweight yet powerful model scaling depth, width, and resolution via compound coefficients. :contentReference[oaicite:5]{index=5}

Both models were fine-tuned using pretrained weights. Training utilized cross-entropy loss optimized via stochastic gradient descent. Evaluation metrics include accuracy, precision, recall, and F1-score. :contentReference[oaicite:6]{index=6}

---

## Evaluation

Model performance was measured on validation and test sets using standard classification metrics: accuracy, precision, recall, and F1-score. (You can insert performance tables or visualizations here, such as confusion matrices or ROC curves.)

---

## Project Structure

```text
├── data/
│   ├── raw/                    # Collected images via download scripts
│   ├── processed/              # After resizing, normalization, augmentation
│
├── scripts/
│   ├── download_attire.py      # Script to gather images
│   ├── download_attire_extended.py  # Extended data collection
│
├── notebooks/
│   ├── exploratory_analysis.ipynb  # Data EDA and visualization
│   ├── training.ipynb              # Training and model diagnostics
│   ├── evaluation.ipynb            # Model evaluation and metrics
│
├── src/
│   ├── model.py                 # Model definitions (ResNet-34, EfficientNet-B0)
│   ├── train.py                 # Training scripts
│   ├── evaluate.py              # Evaluation logic
│   └── utils.py                 # Helpers (metrics, plotting, etc.)
│
├── results/                     # Saved models, logs, performance metrics
│
├── README.md                    # This documentation
└── requirements.txt             # Package dependencies
