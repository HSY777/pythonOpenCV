import cv2

# image = cv2.imread("image/moon.PNG", cv2.IMREAD_ANYCOLOR)
# image = cv2.imread("image/moon.PNG", cv2.IMREAD_GRAYSCALE)
# image = cv2.imread("image/moon.PNG", cv2.IMREAD_COLOR)
# image = cv2.imread("image/moon.PNG", cv2.IMREAD_ANYDEPTH)
# image = cv2.imread("image/moon.PNG", cv2.IMREAD_REDUCED_GRAYSCALE_2)
# image = cv2.imread("image/moon.PNG", cv2.IMREAD_REDUCED_GRAYSCALE_4)
# image = cv2.imread("image/moon.PNG", cv2.IMREAD_REDUCED_GRAYSCALE_8)
# image = cv2.imread("image/moon.PNG", cv2.IMREAD_REDUCED_COLOR_2)
# image = cv2.imread("image/moon.PNG", cv2.IMREAD_REDUCED_COLOR_4)
# image = cv2.imread("image/moon.PNG", cv2.IMREAD_REDUCED_COLOR_8)

height, width, channel = image.shape # imread한 이미지의 정보
print(height, width, channel)

cv2.imshow("Moon", image)
cv2.waitKey()
cv2.destroyAllWindows()

# 이미지의 속성은 크기, 정밀도, 채널을 주요한 속성으로 사용합니다.