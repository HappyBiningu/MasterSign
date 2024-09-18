import cv2
import mediapipe as mp

def start_recognition():
    """
    Start hand gesture recognition using MediaPipe Hands solution
    """
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_drawing = mp.solutions.drawing_utils

    # Initialize video capture from default camera (index 0)
    cap = cv2.VideoCapture(1)
    

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame from BGR to RGB for MediaPipe processing
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Draw hand landmarks on the original frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display the output frame
        cv2.imshow('Hand Gesture Recognition', frame)

        # Exit condition: press 'q' key to quit
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # Release video capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_recognition()