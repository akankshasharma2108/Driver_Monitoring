# Driver Drowsiness and Head Movement Detection System

## Project Overview
This project is an **AI-based Driver Monitoring System** that detects **driver drowsiness and unsafe head movements** using a webcam.

It helps prevent road accidents be alerting the driver when:
- Eyes are closed for too long 
- Head is tilting or nodding 

---

## Problem Statement
Road accidents often happen due to:
- Driver sleep (drowsiness)
- Lack of attention
- Head movement indicating fatigue

This project provides a **real-time and low-cost solution** using computer vision.

---

## Solution
The system:
1. Captures live video from webcam
2. Detects face and facial landmarks
3. Monitors:
   - Eye closure (EAR method)
   - Head movement (tilt detection)
4. Triggers an alert if unsafe behavior is detected

---

## Tech Stack

- **Language:** Python 3
- **Libraries:**
  - OpenCV
  - dlib
  - imutils
  - scipy
  - numpy

---
### Install Dependencies
pip install opencv-python dlib imutils scipy numpy


---

## How to Run
- Webcam will start
- System detects eyes and head movement
- Alert will trigger if drowsiness is detected

---

## Working Principle
- Uses **facial landmark detection**
- Calculates **Eye Aspect Ratio (EAR)**
- Tracks **head angle**
- Applies threshold logic to detect:
  - Drowsiness
  - Distraction

---

## Features
- Real-time monitoring
- Eye closure detection
- Head movement tracking
- Instant alert system
- Simple and efficient

---

## Challenges Faced
- Installing dlib
- Lighting conditions
- False alerts during blinking
- Accurate head tilt detection

---

## Future Improvements
- Add deep learning models
- Detect yawning
- Night vision support
- Mobile app integration
- Vehicle integration

---

## Learning Outcomes
- Computer Vision basics
- Real-time AI systems
- Facial landmark detection
- Debugging and optimization

---

## Conclusion
This project demonstrates how AI can improve road safety by detecting driver drowsiness and distraction in real-time.

---


**Akanksha Sharma**  
B.Tech CSE  
