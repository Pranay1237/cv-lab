import cv2

# Path to the input video file
input_file = 'vid2.mp4'

# Create a VideoCapture object to read the input video
cap = cv2.VideoCapture(input_file)

# Check if the video file was successfully opened
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Read and display each frame of the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If the frame was not successfully read, then we have reached the end of the video
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Wait for 25 milliseconds and check if the user pressed the 'q' key to quit
    if cv2.waitKey(25) == ord('q'):
        break

# Release the VideoCapture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
