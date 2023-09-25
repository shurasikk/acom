import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Can't open the camera")
    exit()

while True:
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    ret, frame = cap.read()
    if not ret:
        print("Can't read the frame")
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('rgb', frame)
    cv2.imshow('hsv', hsv)

cap.release()
cv2.destroyAllWindows()