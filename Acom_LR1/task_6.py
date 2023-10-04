import cv2

img = cv2.imread(r'C:\Users\Asus\Documents\GitHub\acom\Acom_LR1\media\leaf.JPG')
height, width, _ = img.shape

rect_width = 100
rect_height = 500

top_left_x = (width - rect_width) // 2
top_left_y = (height - rect_height) // 2
bottom_right_x = top_left_x + rect_width
bottom_right_y = top_left_y + rect_height

p11=(top_left_x-100, top_left_y)
p12=(top_left_x+300, top_left_y)
p13=((top_left_x+100),bottom_right_y)

cv2.line(img, p11, p12, (255,0,0), 20)
cv2.line(img, p11, p13, (255,0,0), 20)
cv2.line(img, p12, p13, (255,0,0), 20)

p21=(top_left_x-100, bottom_right_y-100)
p22=(top_left_x+300, bottom_right_y-100)
p23=(p12[0]-200, top_left_y-100)

cv2.line(img,p21,p22,(255,0,0), 20)
cv2.line(img, p21, p23, (255,0,0), 20)
cv2.line(img, p22, p23, (255,0,0), 20)

#ROI = img[top_left_y:top_left_y + rect_height, top_left_x:top_left_x + rect_width]

#blur = cv2.GaussianBlur(ROI, (101, 1), 30)
#img[top_left_y:top_left_y + rect_height, top_left_x:top_left_x + rect_width] = blur
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()