import cv2
import numpy as np
import math

# Load Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Start video capture
cap = cv2.VideoCapture(0)

# Counters
eye_closed_frames = 0
alert_threshold_eye = 15    # Frames eyes closed to trigger alert
alert_threshold_head = 15   # Frames head moving too much

# Previous head center
prev_head_center = None
head_movement_counter = 0

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    status = "SAFE TO DRIVE"
    color = (0, 255, 0)  # Green

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # ----- Eye Detection -----
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        if len(eyes) == 0:
            eye_closed_frames += 1
        else:
            eye_closed_frames = 0
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 255, 0), 2)

        # ----- Head Movement Detection -----
        head_center = (x + w // 2, y + h // 2)
        if prev_head_center is not None:
            dx = head_center[0] - prev_head_center[0]
            dy = head_center[1] - prev_head_center[1]
            distance = math.sqrt(dx*dx + dy*dy)

            if distance > 15:  # Threshold for head movement
                head_movement_counter += 1
            else:
                head_movement_counter = 0

        prev_head_center = head_center

        # Draw face rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # ----- Determine Driver Status -----
    if eye_closed_frames >= alert_threshold_eye or head_movement_counter >= alert_threshold_head:
        status = "NOT SAFE TO DRIVE"
        color = (0, 0, 255)  # Red

    # Show status
    cv2.putText(frame, status, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # Display frame
    cv2.imshow('Driver Safety Detection', frame)

    # Quit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()