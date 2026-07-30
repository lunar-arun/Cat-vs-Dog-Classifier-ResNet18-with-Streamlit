# 🐶🐱 Cat vs Dog Classifier using ResNet18

A deep learning web application that classifies images as either **Cat** or **Dog** using a fine-tuned **ResNet18** model. The application is built with **PyTorch** for inference and **Streamlit** for an interactive web interface.

## 🚀 Live Demo

Try the deployed application here:

**https://cat-vs-dog-classifier-resnet18-with-app-lunar.streamlit.app/**

## 📌 Overview

This project demonstrates how transfer learning can be used for image classification. A pretrained **ResNet18** model is fine-tuned to distinguish between cats and dogs, providing fast and accurate predictions from uploaded images.

The application allows users to:
- Upload an image of a cat or dog
- Run inference using a trained ResNet18 model
- View the predicted class instantly through a simple Streamlit interface

## 🛠️ Tech Stack

- Python
- PyTorch
- Torchvision
- Streamlit
- Pillow (PIL)

## 📂 Project Structure

```
.
├── app.py
├── requirements.txt
├── model/
├── assets/
└── README.md
```

> The exact folder structure may vary depending on your project files.

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit app

```bash
streamlit run app.py
```

The application will open in your default browser. If it doesn't, open the local URL displayed in your terminal (typically `http://localhost:8501`).

## 📸 Usage

1. Launch the application.
2. Upload an image of a cat or dog.
3. Wait for the model to process the image.
4. View the predicted class.

## 📖 Model

The classifier is based on **ResNet18**, a convolutional neural network introduced by Microsoft Research. It uses residual connections that enable deeper networks to train effectively while maintaining strong performance on image classification tasks.

## 📄 License

This project is available for educational and learning purposes.
