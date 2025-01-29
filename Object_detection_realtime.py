import cv2
import torch
import numpy as np

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Initialize webcam (adjust index if necessary)
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Set webcam resolution
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Press 'q' to exit.")

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Convert frame to RGB (YOLO expects RGB images)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform inference
    results = model(frame_rgb)

    # Parse results
    detections = results.xyxy[0].numpy()  # Bounding boxes and confidence

    for detection in detections:
        x1, y1, x2, y2, confidence, class_id = detection[:6]
        if confidence > 0.5:  # Confidence threshold
            label = f"{results.names[int(class_id)]} {confidence:.2f}"

            # Draw bounding box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            
            # Display label
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('YOLOv5 Real-Time Object Detection', frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
capture.release()
cv2.destroyAllWindows()
