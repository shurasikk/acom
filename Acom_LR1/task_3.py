import cv2

cap = cv2.VideoCapture(r'C:\Users\Asus\Documents\GitHub\acom\Acom_LR1\media\no41.mp4')

# cv2.CAP_PROP_BRIGHTNESS - яркость (0-1)
# cv2.CAP_PROP_CONTRAST - контраст (0-1)
# cv2.CAP_PROP_SATURATION - насыщенность (0-1)
# cv2.CAP_PROP_HUE - оттенок (0-1)

cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)
cap.set(cv2.CAP_PROP_CONTRAST, 0.8)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
while True:
    # Захват кадра из видеопотока.
    ret, frame = cap.read()

    if not ret:
        print("Конец видео.")
        break

    cv2.imshow("Video", frame)

    # Выход на q.
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break

# Освобождение памяти
cap.release()
cv2.destroyAllWindows()