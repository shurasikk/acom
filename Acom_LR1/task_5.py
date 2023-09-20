import cv2

image_path = r'C:\Users\Asus\Documents\GitHub\acom\Acom_LR1\media\leaf.JPG'
img = cv2.imread(image_path, cv2.IMREAD_COLOR)  # Чтение в оттенках серого
resize = cv2.resize(img, (500, 500))

hsv = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)
hsv_res = cv2.resize(hsv, (500, 500))
cv2.imshow("Original", resize)
cv2.imshow("HSV", hsv_res)
cv2.waitKey(0)