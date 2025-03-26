import cv2

# 이미지 로드 및 출력
image = cv2.imread("./road.jpg")  # 파일 경로에 맞게 변경
cv2.imshow("Road Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
