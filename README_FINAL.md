
# 🧠 Watcher Face Recognition System

Integrated facial recognition system using Raspberry Pi and Seedstudio Watcher, designed for real-time face detection, training, and identification with LED indication.

---

## 📌 Table of Contents
- [Description](#Description)
- [Requirements](#requirements)
- [Hardware Setup](#hardware-setup)
- [Software Installation](#software-installation)
- [Step-by-Step Process](#step-by-step-process)
- [Demo Video](#demo-video)
- [Project Structure](#project-structure)
- [Sample Captures & Output](#Sample-Captures-&-Output)

---

## 🧾 Description
This project is an autonomous system that:
- Captures images via the Seedstudio Watcher over a serial port.
- Saves and organizes images by name.
- Trains a face recognition model using the `face_recognition` library.
- Uses green/red LEDs to indicate recognition results.
- Handles real Base64 images and serial communication.

---

## ⚙️ Requirements

**Hardware:**
- Raspberry Pi (recommended: 3B+, 4)
- Seedstudio Watcher
- Connected green/red LEDs to GPIO (pins 23 and 24)

**Software / Libraries:**
```bash
sudo apt update
sudo apt install python3-pip python3-opencv libatlas-base-dev libjasper-dev libqtgui4 python3-pyqt5 libqt4-test -y

pip3 install face_recognition
pip3 install imutils
pip3 install opencv-python
pip3 install numpy
pip3 install Pillow
pip3 install pyserial
pip3 install RPi.GPIO
```

## 🔧 Hardware Setup
1. In the SenseCraft app connect your Watcher to your phone via Bluetooth.
   Quick Start Guide: https://wiki.seeedstudio.com/getting_started_with_watcher/.
   For a full app guide you can check: https://wiki.seeedstudio.com/sensecap_app_introduction/

2. In the chat with your device in the app create a new task and use the following settings:
   - ![Task_1](https://imgur.com/7QItBro)
   - ![Task_2](https://imgur.com/O6Dkijm)
3. Connect the Watcher to the Raspberry Pi via USB or UART.
   Watcher UART wiring:

   ![Wiring_diag](https://imgur.com/qPzndiU)

4. Wire the LEDs:
   - Red: GPIO 24
   - Green: GPIO 23
5. Ensure `/dev/ttyAMA0` or `/dev/ttyACM0` is the active serial port.
```bash
   ls /dev/ttyAMA*
```

   ![dev_check](https://imgur.com/tcNM9GK)

---

## 💻 Project Installation
```bash
git clone https://github.com/rndbg/watcher.git
cd watcher
```

---

## 🚀 Step-by-Step Process

### 1. Capture Images (`image_capture.py`)
```bash
python3 image_capture.py
```
- Starts listening to the serial port.
- Receives JSON with `big_image` → decodes and saves the image.
- Images are stored in `TrainingImages/<name>`.

### 2. Train Model (`model_training.py`)
```bash
python3 model_training.py
```
- Scans the `TrainingImages` folder.
- Extracts face encodings.
- Creates `encodings.pickle`.

### 3. Real-Time Recognition (`facial_recognition.py`)
```bash
python3 facial_recognition.py
```
- Listens for images via serial port.
- Recognizes faces and activates LED based on result.

---

## 🎥 Demo Video
📌 *[Add YouTube/Vimeo demo link here]*

---

## 📂 Project Structure
```
project/
├── image_capture.py
├── model_training.py
├── facial_recognition.py
├── TrainingImages/
│   └── <person_name>/
├── received_images/
├── encodings.pickle
```


## 📷 Sample Captures & Output

### Capturing Images via Serial Port
![Image Capture](https://imgur.com/pQGoFO3)

### Real-Time Facial Recognition
![Recognition Output](https://imgur.com/czMtoVw)

### Project File Structure on Raspberry Pi
![Project Structure](https://imgur.com/0WI458X)


---



