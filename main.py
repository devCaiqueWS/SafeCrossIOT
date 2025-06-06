import cv2
import mediapipe as mp
from gestures.gesture_utils import detect_hand_gesture

# Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

def show_alert(frame, message, color=(0, 0, 255)):
    cv2.putText(frame, message, (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 3)

cap = cv2.VideoCapture("samples/dark_environment_test.mp4") 
cv2.namedWindow("SafeCross Vision - Gestos", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("SafeCross Vision - Gestos", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        gesture = detect_hand_gesture(results.multi_hand_landmarks)

        if gesture == "open":
            show_alert(frame, "1 OPEN HAND - PARE!")
        elif gesture == "fist":
            show_alert(frame, "FIST - ALERTA DESATIVADO", (0, 255, 0))
        elif gesture == "emergency":
            show_alert(frame, "2 HANDS UP - EMERGENCIA DETECTADA!")
        elif gesture == "pointing":
            show_alert(frame, "GESTO DE DIRECAO")

        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("SafeCross Vision - Gestos", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
