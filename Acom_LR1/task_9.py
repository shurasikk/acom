import cv2

cap = cv2.VideoCapture(1)


while True:
    ret, frame = cap.read()

    if not ret:
        print("Конец видео.")
        break
    cv2.imshow("Video", frame)

    # Выход на q.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Освобождение памяти
cap.release()
cv2.destroyAllWindows()

