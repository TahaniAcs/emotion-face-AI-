# 🎭 AI Emotion Mirror

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![DeepFace](https://img.shields.io/badge/AI-DeepFace-orange?style=for-the-badge)

> A real-time computer vision application that detects faces and analyzes human emotions using Deep Learning.

## 📖 About The Project
**AI Emotion Mirror** is an interactive Python application that turns your webcam into a smart mirror. It uses the powerful **DeepFace** library to analyze facial expressions in real-time and displays the user's current emotion (e.g., Happy, Sad, Surprise, Neutral) directly on the video feed.

This project demonstrates the integration of **Computer Vision** with **Deep Learning** models to understand human behavior.

## ✨ Key Features

* **⚡ Real-Time Analysis:** Instantly processes video frames from the webcam using OpenCV.
* **🧠 Deep Learning Powered:** Utilizes pre-trained models via `DeepFace` for high-accuracy emotion detection.
* **😊 7 Emotions Support:** Capable of detecting: Angry, Disgust, Fear, Happy, Sad, Surprise, and Neutral.
* **🛡️ Robust Error Handling:** Automatically handles cases where no face is detected ("Waiting for face...").

## 🛠️ Technologies Used

* **Language:** Python 3
* **Computer Vision:** [OpenCV (cv2)](https://opencv.org/)
* **AI Framework:** [DeepFace](https://github.com/serengil/deepface)

## 🚀 How to Run Locally

To run this project on your machine, follow these steps:

1.  **Clone the repository:**
    ```bash
   git clone https://github.com/TahaniAcs/emotion-face-AI-.git
    ```

2.  **Install the required libraries:**
    ```bash
    pip install opencv-python deepface tf-keras
    ```

3.  **Run the script:**
    ```bash
    python emotion_app.py
    ```
    *(Note: The first run might take a moment to download the AI weights).*

4.  **Exit:**
    Press `q` on your keyboard to close the application.

## 📸 Screenshots

## 👥 Credits
Developed by **Tahani Althobiti**.
