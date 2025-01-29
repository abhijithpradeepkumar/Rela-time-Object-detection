# Real-Time Object Detection and Tracking with YOLOv5

Overview

This project implements real-time object detection using YOLOv5 and OpenCV with a webcam. It detects multiple objects in real-time, drawing bounding boxes and labels on detected objects. The project is ideal for robotics, automation, and STEM education.

Features

Uses YOLOv5 for real-time object detection

Runs on a laptop webcam (Linux/macOS/Windows compatible)

Efficient and Fast inference using PyTorch

Tracks multiple objects simultaneously

Easy to extend (custom dataset, additional features)

Installation

Prerequisites

Ensure you have Python 3.7 or later installed.

Install Dependencies

pip install opencv-python torch torchvision numpy ultralytics

Clone the Repository

git clone https://github.com/your-username/real-time-object-detection.git
cd real-time-object-detection

Running the Project

Run the Python script to start real-time detection:

python object_detection_yolo.py

Usage

The script will open your webcam and start detecting objects.

Press 'q' to quit the application.

How It Works

Load YOLOv5: Downloads and initializes the pre-trained yolov5s model.

Capture Video: Uses OpenCV to access the webcam.

Process Frames: Converts frames to RGB and passes them to YOLOv5.

Detect Objects: Extracts bounding boxes, confidence scores, and class labels.

Draw Bounding Boxes: Displays detected objects in real-time.

Customization

Modify the confidence threshold in the script to adjust detection sensitivity.

Train YOLOv5 on a custom dataset to detect specific objects.

Implement robotics integration by using bounding box coordinates for control.

Future Enhancements
Implement object tracking for motion analysis.
Deploy on embedded devices (Jetson Nano, Raspberry Pi).

License

This project is licensed under the MIT License.
