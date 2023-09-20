import math

import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Asus\Documents\GitHub\acom\Acom_LR1\media\leaf.JPG')
height, width, _ = img.shape
center_x = width // 2
center_y = height // 2
#center_pixel = img[center_x, center_y]

(b, g, r) = img[np.int16(center_y), np.int16(center_x)]
print("Color at center pixel is - Red: {}, Green: {}, Blue: {}".format(r, g, b))

def closest_color(x,y):
    colors = {"0": (0, 0, 255), "1": (0, 255, 0), "2": (255, 0, 0)}
    min_distance = float('inf')
    closest = None
    (b, g, r) = img[np.int16(y), np.int16(x)]
    for color_name, color_value in colors.items():
        distance = sum(((r,g,b) - np.array(color_value)) ** 2)
        if math.sqrt(distance) < min_distance:
            min_distance = math.sqrt(distance)
            closest = color_name

    return closest


closest = closest_color(center_x, center_y)
print(closest)

rect_width = 100
rect_height = 500

top_left_x = (width - rect_width) // 2
top_left_y = (height - rect_height) // 2
bottom_right_x = top_left_x + rect_width
bottom_right_y = top_left_y + rect_height
if closest == "0":
    cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), -1)
if closest == "1":
    cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), -1)
if closest == "2":
    cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 0, 0), -1)

rect_width = 500
rect_height = 100

top_left_x = (width - rect_width) // 2
top_left_y = (height - rect_height) // 2
bottom_right_x = top_left_x + rect_width
bottom_right_y = top_left_y + rect_height
if closest == "0":
    cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 0, 255), -1)
if closest == "1":
    cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), -1)
if closest == "2":
    cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 0, 0), -1)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # Окно с изменяемым размером
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()