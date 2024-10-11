import cv2
import numpy as np

# Initialize video capture
cap = cv2.VideoCapture(0)

# Set the camera resolution to maximum (you can adjust these values)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640   dfsDdgfgdsgddgs)  # Example: 1920 for Full HD
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Example: 1080 for Full HD

# Allow time to set up
print("Please position your camera to capture the background...")
cv2.waitKey(5000)

# Capture the background
ret, background = cap.read()
background = cv2.flip(background, 1)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally for a mirror effect

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define ranges for parrot colors (example values)
    lower_green = np.array([90, 100, 100])
    upper_green = np.array([130, 255, 255])
    
    # Create a mask for the green color
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Invert the mask
    mask_inv = cv2.bitwise_not(mask_green)

    # Use the mask to extract the background where the green is not present
    background_area = cv2.bitwise_and(background, background, mask=mask_green)
    
    # Use the inverse mask to extract the foreground
    foreground_area = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine the background and the foreground areas
    result = cv2.add(background_area, foreground_area)

    # Display the resulting frame
    cv2.imshow('Invisible Cloak Effect (Parrot Colors)', result)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
