import cv2
import numpy as np

# 이미지 로드 및 그레이스케일 변환
image = cv2.imread("road.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 가우시안 블러 적용
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny Edge Detection
edges = cv2.Canny(blur, 50, 150)

# 결과 출력
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
