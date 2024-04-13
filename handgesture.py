import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation
mp_gesture_recognizer = mp.solutions.gesture_recognizer

# Initialize MediaPipe gesture recognizer solution.
gesture_recognizer = mp_gesture_recognizer.GestureRecognizer(
    model_name="HandGestureModel"
)

# Initialize MediaPipe selfie segmentation solution for hand image segmentation.
selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation()

# Initialize MediaPipe drawing solution.
drawing_utils = mp_drawing.DrawingSpec()

# Process image frames and classify hand gestures.
def process_frame(image):
    with gesture_recognizer:
        results = gesture_recognizer.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks on image.
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_gesture_recognizer.HAND_CONNECTIONS)

        # Get top detected gesture.
        top_gesture = results.gesture_result[0].score
        if top_gesture > 0.7:
            print("Detected gesture:", results.gesture_result[0].name)

# Function to load image from file and process it with MediaPipe.
def load_image(filename):
    image = cv2.imread(filename)
    results = process_frame(image)
    cv2.imshow("Hand Sign Detection", image)
    cv2.waitKey(0)

# Load image from file and process it with MediaPipe.
load_image("hand_sign.jpg")