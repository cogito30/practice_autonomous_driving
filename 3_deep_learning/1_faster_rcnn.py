import torch
import torchvision
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
import cv2

# Faster R-CNN 모델 불러오기 (사전 학습된 모델)
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()  # 평가 모드

# 이미지 변환 (PyTorch Tensor로 변환)
transform = transforms.Compose([
    transforms.ToTensor(),  # 이미지 -> Tensor 변환
])

# 이미지 불러오기
image_path = "road.jpg"  # 테스트할 이미지
image = Image.open(image_path).convert("RGB")
image_tensor = transform(image).unsqueeze(0)  # 배치 차원 추가

# 모델 예측
with torch.no_grad():
    predictions = model(image_tensor)

# 예측 결과 확인
pred_boxes = predictions[0]['boxes'].cpu().numpy()  # 바운딩 박스 좌표
pred_labels = predictions[0]['labels'].cpu().numpy()  # 클래스 레이블
pred_scores = predictions[0]['scores'].cpu().numpy()  # 확률 점수

# 신뢰도 0.5 이상인 박스만 선택
threshold = 0.5
filtered_boxes = pred_boxes[pred_scores > threshold]
filtered_labels = pred_labels[pred_scores > threshold]
filtered_scores = pred_scores[pred_scores > threshold]

# 이미지 로드 및 OpenCV 변환
image_cv = cv2.imread(image_path)
image_cv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)

# 클래스 이름 불러오기 (COCO 데이터셋 기준)
COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'street sign', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant',
    'bear', 'zebra', 'giraffe', 'hat', 'backpack', 'umbrella', 'shoe', 'eye glasses',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite',
    'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'plate', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana',
    'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut',
    'cake', 'chair', 'couch', 'potted plant', 'bed', 'mirror', 'dining table',
    'window', 'desk', 'toilet', 'door', 'tv', 'laptop', 'mouse', 'remote', 'keyboard',
    'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'blender',
    'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

# 바운딩 박스 그리기
for box, label, score in zip(filtered_boxes, filtered_labels, filtered_scores):
    x1, y1, x2, y2 = map(int, box)
    class_name = COCO_INSTANCE_CATEGORY_NAMES[label]
    text = f"{class_name}: {score:.2f}"

    # 박스 그리기
    cv2.rectangle(image_cv, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(image_cv, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# 이미지 출력
plt.figure(figsize=(10, 6))
plt.imshow(image_cv)
plt.axis("off")
plt.show()
