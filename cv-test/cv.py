import cv2

filename = "test.png"

img = cv2.imread(filename)

img[:, :, 1] = 0  # clear green channel

cv2.imwrite("out.png", img)
