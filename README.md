# neurosync-project-medical-hackathon-
NeuroSync: An AI-powered soft-robotic exoskeleton for stroke rehabilitation. It merges Neuroscience (Hebbian Learning &amp; Neuroplasticity) with Psychology (Gamified Dopaminergic Reward) to accelerate motor recovery. Features a secure IoMT architecture with AES-256 encryption.
# 🧠 NeuroSync: AI-Powered Soft-Robotic Exoskeleton for Stroke Rehabilitation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Unity](https://img.shields.io/badge/Unity-2022.3-black)](https://unity.com/)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Hardware](https://img.shields.io/badge/Hardware-ESP32%20%7C%20Servo-red)](https://espressif.com/)
[![Security](https://img.shields.io/badge/Security-AES--256-green)]()

> **"Where Robotics Meets Neuroplasticity."**
> A gamified, secure, and AI-assisted rehabilitation system designed to accelerate motor recovery in stroke patients through Hebbian Learning principles.

---

## 📖 Table of Contents
- [Project Overview](#-project-overview)
- [The Science (Neuroscience & Psychology)](#-the-science-behind-neurosync)
- [System Architecture](#-system-architecture)
- [Key Features](#-key-features)
- [Security & Compliance](#-security--compliance)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)

---

## 🔭 Project Overview
**NeuroSync** is a low-cost, soft-robotic exoskeleton glove designed to assist patients with hand paralysis (hemiplegia) resulting from stroke or spinal cord injury. 

Unlike traditional passive physiotherapy, NeuroSync utilizes **Active-Assisted Robotic Therapy** combined with **Immersive Gamification**. The system detects the patient's faint muscle signals (via Flex/EMG sensors) or visual intent (via Computer Vision) and actuates the glove to complete the movement, simultaneously controlling a video game.

---

## 🧬 The Science Behind NeuroSync

This project is not just a mechanical tool; it is a **Neuro-Cognitive Rehabilitation Device** built on two core scientific pillars:

### 1. Neuroscience: Hebbian Learning & Neuroplasticity
* **Principle:** *"Neurons that fire together, wire together."*
* **Implementation:** By synchronizing the patient's *intent* (brain signal) with the *physical movement* (robot actuation) and *visual feedback* (game action), NeuroSync closes the sensorimotor loop.
* **Proprioceptive Feedback:** The glove physically forcing the fingers to curl sends sensory data back to the brain, stimulating the **Somatosensory Cortex**, which helps rewire damaged neural pathways around the stroke lesion.

### 2. Psychology: Operant Conditioning & Dopaminergic Reward
* **Principle:** Reinforcement Learning through immediate reward.
* **The Problem:** Traditional therapy is repetitive and boring, leading to "Learned Non-Use."
* **The Solution:** We gamified the therapy (e.g., controlling a "Flappy Bird" clone).
* **Mechanism:** Every successful hand closure keeps the bird flying. This success triggers a **Dopamine Release** in the brain's Striatum. Dopamine acts as a neuro-modulator that strengthens synaptic connections, making the brain "learn" the movement faster and reducing patient fatigue.

---

## ⚙️ System Architecture

### 1. Input Layer (The Senses)
* **Physical:** Flex Sensors / EMG Sensors (detects muscle contraction).
* **Visual (AI):** Python + MediaPipe (Computer Vision) tracks hand skeleton coordinates via webcam for contactless therapy.

### 2. Processing Layer (The Brain)
* **Microcontroller:** ESP32 (Dual Core) handles sensor data acquisition and servo control.
* **Signal Processing:** Raw analog signals are filtered (Moving Average Filter) to remove noise.
* **Encryption:** Data is encrypted before transmission.

### 3. Output Layer (The Action)
* **Actuation:** High-torque MG996R Servo Motors pull tendon cables (Braided Fishing Line) to flex the fingers.
* **Visual Feedback:** Unity 3D Game Engine receives data via UDP Socket to control the virtual avatar.

---

## 🚀 Key Features

* **🕹️ Gamified Therapy:** Turns boring rehab reps into engaging gameplay.
* **🤖 Soft-Robotic Design:** Lightweight, 3D-printed mounts on a breathable glove for safety and comfort.
* **👁️ Computer Vision Fallback:** Can operate without physical sensors using just a laptop camera.
* **📡 IoT Dashboard:** Real-time data logging for doctors to monitor progress remotely.
* **🧠 AI Fatigue Detection:** (Beta) Analyzes hand tremors to auto-stop therapy if the patient is tired.

---

## 🔐 Security & Compliance
In the era of IoMT (Internet of Medical Things), security is paramount.
* **AES-256 Encryption:** All sensor data transmitted between the glove and the PC is encrypted using the Advanced Encryption Standard (AES).
* **Integrity:** Prevents Man-in-the-Middle (MITM) attacks where hackers could alter motor commands.
* **DPDP Act Ready:** Designed with Indian Digital Personal Data Protection principles in mind.

---

## 💻 Technology Stack

| Domain | Tech Used |
| :--- | :--- |
| **Hardware** | ESP32, MG996R Servos, Flex Sensors, PCA9685 Driver |
| **Firmware** | C++ (Arduino IDE) |
| **Game Engine** | Unity 3D (C#) |
| **AI/CV** | Python, OpenCV, MediaPipe |
| **Communication** | UDP Sockets (Low Latency), Wi-Fi |
| **Security** | PyCryptodome (AES Implementation) |

---

## 📦 Installation

### Prerequisites
* Python 3.10+
* Unity Hub 2021+
* Arduino IDE

### Step 1: Clone Repository
```bash
git clone [https://github.com/your-username/NeuroSync.git](https://github.com/your-username/NeuroSync.git)
cd NeuroSync

### Step 2: Install Python Dependencies
Bash
pip install opencv-python mediapipe pycryptodome

### Step 3: Flash the ESP32
Open Firmware/NeuroSync_ESP32.ino in Arduino IDE and upload to your board.

### Step 4: Run the System
Open the Unity Project and press Play.

Run the Python script: python AI_Engine/brain.py

🏆 Achievements
National Finalist: [first global hackathon on medical robotics] (2025)

Showcased at: AMTZ Medical Robotics Hackathon,visakhapatnam

🤝 Contributors
[kavibharathi] - Lead Developer & Robotics Engineer



📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
