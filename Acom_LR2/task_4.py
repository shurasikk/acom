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

    if area > 0:
        width = height = int(np.sqrt(area))
        c_x = int(moments["m10"] / moments["m00"])
        c_y = int(moments["m01"] / moments["m00"])
        color = (0, 0, 0)
        thickness = 1
        cv2.rectangle(frame,
            (c_x - (width // 10), c_y - (height // 10)),
            (c_x + (width // 10), c_y + (height // 10)),
            color, thickness)

    cv2.imshow('HSV_frame', hsv)
    cv2.imshow('Result_frame', frame)

    # нажатие клавиши esc для выхода из цикла
    if cv2.waitKey(1) & 0xFF == 27:
        break

print("Площадь объекта:", area)

cap.release()
cv2.destroyAllWindows()
