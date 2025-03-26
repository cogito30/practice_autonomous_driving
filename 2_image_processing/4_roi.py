import cv2
import numpy as np

# 이미지 로드 및 전처리
image = cv2.imread("road.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

# Hough Transform을 활용한 직선 검출
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=100, maxLineGap=50)

# 검출된 선을 원본 이미지에 표시
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)

def region_of_interest(img):
    height, width = img.shape[:2]
    mask = np.zeros_like(img)
    
    # 관심 영역 설정 (삼각형 형태)
    polygon = np.array([[
        (0, height),
        (width, height),
        (width // 2, height // 2)
    ]], np.int32)
    
    cv2.fillPoly(mask, polygon, 255)
    roi = cv2.bitwise_and(img, mask)
    return roi

roi_image = region_of_interest(edges)
cv2.imshow("ROI", roi_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
