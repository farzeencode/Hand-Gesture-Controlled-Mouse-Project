import cv2
import mediapipe as mp
import time
import math
import autopy
pTime=0

# Initialize MediaPipe Hands
capture_hands = mp.solutions.hands.Hands()
drawing_option = mp.solutions.drawing_utils

# OpenCV Video Capture
camera = cv2.VideoCapture(0)

# Set the screen width and height for mouse control
screen_width, screen_height = autopy.screen.size()

# Set a threshold for the click detection
click_threshold = 30
smoothing_factor = 0.5

# Initialize the previous mouse position
prev_mouse_x, prev_mouse_y = autopy.mouse.location()

while True:
    # Read the camera frame
    ret, image = camera.read()
    image = cv2.flip(image, 1)  # Flip the frame horizontally
    image_height, image_width, _ = image.shape

    # Convert BGR to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    output_hands = capture_hands.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks

    # Draw landmarks and circles on the detected hand(s)
    if all_hands:
        for hand in all_hands:
            # Draw landmarks
            drawing_option.draw_landmarks(image, hand, mp.solutions.hands.HAND_CONNECTIONS)

            # Get the index finger tip and thumb tip coordinates
            index_finger_tip = hand.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP.value]
            thumb_tip = hand.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP.value]
            # to pixel coordinates of two specific landmarks
            x = int(index_finger_tip.x * image_width)
            y = int(index_finger_tip.y * image_height)
            a = int(thumb_tip.x * image_width)
            b=  int(thumb_tip.y * image_height)

            # Draw circles on the fingertips
            cv2.circle(image, (x, y), 18, (0, 255, 255), -1)
            cv2.circle(image, (a, b), 18, (0, 255, 255), -1)

            # Calculate the distance between index finger tip and thumb tip
            distance = math.sqrt((a - x)**2 + (b - y)**2)

            # to Move the mouse cursor with the index finger when it is up
            if y < b:
                # Smooth the mouse movement
                smoothed_x = smoothing_factor * x + (1 - smoothing_factor) * prev_mouse_x
                smoothed_y = smoothing_factor * y + (1 - smoothing_factor) * prev_mouse_y

                autopy.mouse.move(smoothed_x * screen_width / image_width, smoothed_y * screen_height / image_height)

                # Update the previous mouse position
                prev_mouse_x, prev_mouse_y = smoothed_x, smoothed_y

            # Check if the thumb and index finger are touching, and perform a click
            if y < b and distance < click_threshold:
                if not clicked:
                    autopy.mouse.click()
                    clicked = True
                    cv2.putText(image, "Mouse Clicked!", (20, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            else:
                clicked = False

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(image, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)

    # Display the frame
    cv2.imshow("Hand movement video capture", image)

    # Break the loop when 'ESC' is pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the capture and close all windows
camera.release()
cv2.destroyAllWindows()
