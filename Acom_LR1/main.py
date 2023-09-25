import cv2

image_path = r'C:\Users\Asus\Documents\GitHub\acom\Acom_LR1\media\leaf.JPG'
img1 = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(image_path, cv2.IMREAD_LOAD_GDAL)
img3 = cv2.imread(image_path, cv2.IMREAD_COLOR)
if img1 is not None:
    cv2.namedWindow(f"Image1", cv2.WINDOW_NORMAL)
    cv2.imshow(f"Image1", img1)
    cv2.namedWindow(f"Image2", cv2.WINDOW_AUTOSIZE)
    cv2.imshow(f"Image2", img2)
    cv2.namedWindow(f"Image3", cv2.WINDOW_FULLSCREEN)
    cv2.imshow(f"Image3", img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Не получилось открыть изображение в этом формате")
