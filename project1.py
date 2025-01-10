import cv2

# Initialize face detection using Haar Cascade
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start video capture
video_cap = cv2.VideoCapture(0)

while True:
    ret, video_data = video_cap.read()  # Read a frame from the video capture
    if not ret:
        break

    # Display the video feed
    cv2.imshow("video_live", video_data)

    # Exit the loop when the 'a' key is pressed
    if cv2.waitKey(10) == ord("a"):
        break

# Release resources
video_cap.release()
cv2.destroyAllWindows()
