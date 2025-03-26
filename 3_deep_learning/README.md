# Deep Learning

## 학습 목표
- CNN(Convolutional Neural Network): 이미지 분석을 위한 딥러닝 모델
- YOLO(You Only Look Once): 실시간 객체 탐지 모델
- OpenCV + YOLO 사용법: 차량, 보행자 탐지
- 실시간 객체 탐지: 웹캠을 활용한 실시간 인식
- Torchvision 모델 사용법: YOLO, Faster R-CNN, SSD

## 1. CNN 개념 & Object Detection 모델
- CNN은 이미지 데이터를 분석하는데 최적화된 신경망
- YOLO도 CNN 기반으로 동작

(CNN 주요개념)
- Convolution Layer: 이미지 특징 추출
- Pooling Layer: 크기 축소 및 연산 최적화
- Fully Connected Layer: 최종 분류 수행

(YOLO vs Faster RCNN)
- YOLO: 한 번의 연산으로 객체 탐지
- Faster RCNN: 두 단계로 나누어 탐지
=> 실시간 분석의 경우 YOLO가 적합

## 2. YOLO 활용
```
pip install opencv-python numpy
wget https://pjreddie.com/media/files/yolov3.weights
wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg
wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names
```

## 3. YOLO로 이미지에서 객체 탐지
- 차량, 보행자 등 객체 탐지
- 웹 캠을 사용한 실시간 탐지

## 4. PyTorch 모델 사용법
- torchvision, torch 설치

(모델 학습 및 테스트 과정)
1. 모델 불러오기
2. 이미지 입력 및 전처리
3. 모델을 활용한 객체 탐지 실행
4. 객체 탐지 결과 시각화

(커스텀 데이터셋으로 학습 및 테스트)
1. 데이터 라벨링: LabelImg 같은 툴로 바운딩 박스 생성
2. 데이터 로더 작성: torch.utils.data.Dataset을 활용하여 커스텀 데이터셋 구축
3. 모델 학습: torchvision.models.detection.FasterRCNN을 사용하여 모델 훈련