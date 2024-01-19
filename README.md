Hand Gesture Mouse Control with OpenCV and MediaPipe
This repository contains a Python script that allows users to control the mouse cursor and perform clicks using hand gestures captured through a webcam. The script uses the MediaPipe library for hand tracking and OpenCV for image processing.

Features:
Real-time Hand Tracking: Utilizes the MediaPipe Hands module to detect and track hand landmarks in real-time from the webcam feed.

Mouse Cursor Control: Moves the mouse cursor based on the position of the index finger, providing a natural and intuitive control mechanism.

Click Detection: Detects a click gesture by checking the proximity of the thumb and index finger, enabling users to perform mouse clicks through hand gestures.

Smooth Mouse Movement: Implements a smoothing factor for mouse movement to ensure a more fluid and user-friendly experience.

Frame Rate Display: Shows the frames per second (FPS) on the video feed to monitor the performance of the hand tracking and mouse control.

Requirements:
Python 3.x
OpenCV
Mediapipe
Autopy
How to Use:
Install the required dependencies by running:

bash
Copy code
pip install opencv-python mediapipe autopy
Run the script:

bash
Copy code
python hand_gesture_mouse.py
Interact with the webcam using hand gestures as described in the script.

Configuration:
Adjust the click_threshold variable to fine-tune the sensitivity of click detection based on your hand size and camera resolution.

Modify the smoothing_factor for mouse movement to achieve the desired level of smoothness.

Notes:
Press 'ESC' to exit the application.
