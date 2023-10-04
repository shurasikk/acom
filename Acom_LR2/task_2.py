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

    # применение маски на кадр(побитовая операция И между изображениями)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('HSV_video', hsv)
    cv2.imshow('Result_video', res)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# освобождение ресурсов окна
cap.release()
cv2.destroyAllWindows()