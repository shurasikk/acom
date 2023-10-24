import cv2
import numpy as np

# объект VideoCapture для подключения к IP-камере
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # определение диапазона красного цвета в HSV
    lower_red = np.array([0, 100, 0])
    upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    moments = cv2.moments(mask)

    area = moments['m00']

    _, thresh = cv2.threshold(mask, 127, 255, 0)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if 5000 < area < 1000000:  # Фильтр по размеру контура
            M = cv2.moments(contour)

            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                color = (0,255,0)
                thickness = 3
                cv2.line(frame, (cx - 20, cy), (cx + 20, cy), color, thickness)
                cv2.line(frame, (cx, cy - 20), (cx, cy + 20), color, thickness)

    cv2.imshow('HSV_frame', hsv)
    cv2.imshow('Result_frame', frame)

    # нажатие клавиши esc для выхода из цикла
    if cv2.waitKey(1) & 0xFF == 27:
        break

print("Площадь объекта:", area)

cap.release()
cv2.destroyAllWindows()
