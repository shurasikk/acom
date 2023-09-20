import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Ошибка при открытии вебкамеры.")
    exit()

output_file = "task_7.avi"  # Имя выходного файла
frame_width = int(cap.get(3))  # Ширина кадра
frame_height = int(cap.get(4))  # Высота кадра
fps = 30.0  # Количество кадров в секунду

center_x = frame_width // 2
center_y = frame_height // 2
ret, frame = cap.read()
center_pixel = frame[center_y, center_x]

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

while True:

    ret, frame = cap.read()

    if not ret:
        print("Ошибка при захвате кадра.")
        break

    rect_width = 100  # Ширина прямоугольника
    rect_height = 300  # Высота прямоугольника

    top_left_x = (frame_width - rect_width) // 2
    top_left_y = (frame_height - rect_height) // 2
    bottom_right_x = top_left_x + rect_width
    bottom_right_y = top_left_y + rect_height

    out.write(frame)

    cv2.imshow("Webcam Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()