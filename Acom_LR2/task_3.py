import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # определение диапазона красного цвета в HSV
    min_red = np.array([0, 100, 0])
    max_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, min_red, max_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((10, 10), np.uint8)
    open = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel)
    close = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('Opening', open)
    cv2.imshow('Closing', close)

    # нажатие клавиши esc для выхода из цикла
    if cv2.waitKey(1) & 0xFF == 27:
        break

# освобождение ресурсов окна
cap.release()
cv2.destroyAllWindows()