import cv2
# import numpy as np (no use)
from matplotlib import pyplot as plt
# pip install opencv-python
img = cv2.imread('skull.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(2, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title('Gray')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3)
plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4)
plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y')
plt.xticks([])
plt.yticks([])

plt.show()
