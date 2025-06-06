def get_fingers_up(hand_landmarks):
    tips = [8, 12, 16, 20]
    up = 0
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            up += 1
    return up

def detect_hand_gesture(multi_hand_landmarks):
    gestures_detected = []

    if len(multi_hand_landmarks) == 1:
        hand = multi_hand_landmarks[0]
        fingers_up = get_fingers_up(hand)

        if fingers_up >= 4:
            return "open"
        elif fingers_up == 0:
            return "fist"

        # Gesto de apontar com dedo indicador
        if hand.landmark[8].y < hand.landmark[6].y and all(
            hand.landmark[i].y > hand.landmark[i - 2].y for i in [12, 16, 20]
        ):
            return "pointing"

    elif len(multi_hand_landmarks) == 2:
        left = multi_hand_landmarks[0].landmark
        right = multi_hand_landmarks[1].landmark

        # Gesto de emergência: braços levantados (pulsos abaixo dos dedos)
        if left[0].y > left[8].y and right[0].y > right[8].y:
            return "emergency"

        # Gesto de bloqueio: mãos próximas na horizontal
        distance = abs(left[8].x - right[8].x)
        vertical_distance = abs(left[8].y - right[8].y)

        if distance < 0.15 and vertical_distance < 0.1:
            return "block"

    return "unknown"
