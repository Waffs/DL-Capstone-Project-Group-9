
# 🇳🇬 Nigerian Traditional Attire Image Classifier (Deep Learning Capstone)

This project is a computer vision model designed to classify Nigerian clothing groups (e.g., Hausa, Fulani, Igbo, Yoruba) based on images using **EfficientNet-B0**, **ResNet34** and **PyTorch**. It was trained in Google Colab and deployed using a simple **Gradio** web interface.

---

## 🔍 Project Overview

- **Model**: EfficientNet-B0 (pre-trained)
- **Dataset**: Custom Nigerian Traditional Attire image dataset (`data_split/train`, `val`, `test`)
- **Accuracy**: Achieved 92% validation accuracy
- **Deployment**: Gradio web app (local and online)
- **Frameworks**: PyTorch, torchvision, Gradio

---

## 📁 Folder Structure

```
.
├── data_split/
│   ├── train/
│   ├── val/
│   └── test/
├── ethnic_classifier_gradio_app.py
├── ethnic_classifier_efficientnetb0.pth
├── dl_capstone_project_effientnetb0.ipynb
└── README.md
```


---

## 🚀 How to Run Code

### ⚙️ 1. Set Up Environment

Install the required packages:

```bash
pip install torch torchvision gradio efficientnet_pytorch
```

---

### 🧠 2. Train Model (Optional)

If you want to train the model from scratch:

- Open `dl_capstone_project_efficientnetb0.ipynb` in **Google Colab**
- Make sure your dataset is uploaded or mounted via Google Drive
- Run all cells to train the model and save the best weights as `efficientnetb0_nigerian_attire_classifier.pth`

---

### 💾 3. Load Trained Model

Download `efficientnetb0_nigerian_attire_classifier.pth` from Colab and place it in your working directory.

---

### 🌍 4. Run Local Gradio App

Start your classifier with:

```bash
python ethnic_classifier_gradio_app.py
```

Then open [http://127.0.0.1:7860](http://127.0.0.1:7860) in your browser to upload an image and view the prediction.

---

## 🖼️ Example Prediction

Upload a face image and get a prediction like:

```
Prediction: Fulani
```

---

## 💡 Notes

- Model trained with `manual_seed=42` for reproducibility
- EfficientNet-B0 is used for its accuracy and speed on limited compute
- The classifier uses `softmax` outputs and `torch.max` for prediction

---

## 📦 Requirements

- Python 3.8+
- torch
- torchvision
- gradio
- efficientnet_pytorch

---

## 🤝 Authors

Project developed by Group 9 — Arewa Data Science Fellowship Capstone Team  
- Naziru Abdussalam Ibrahim
- Abdulwasiu Bamidele Popoola
- Ayodeji Akande
- Shamsu Abdullahi
- Abubakar Sadiq Sulaiman
- Taiwo Abbas
- Ahmad Saad 

---

## 🏁 Future Work

- Deploy to Hugging Face or Render
- Improve dataset balance and diversity
- Add mobile/web camera support to app

---
https://drive.google.com/file/d/12sFm2jiuA5zwIWZWc-teWnniKYkEJzqX/view?usp=sharing