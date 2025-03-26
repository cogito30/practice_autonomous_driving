# Autonomous Driving

## Index
1. 기초 개념 학습
2. 센서 데이터 처리 및 영상 인식
3. 주행 알고리즘 구현
4. 시뮬레이션 및 실제 환경 테스트

## 1. 기초 개념 학습
(수학 및 물리 기초)
- 선형대수: 행렬 연산, 벡터 연산
- 미분과 적분: 경사하강법, 최적화
- 확률 및 통계: 베이지안 확률, 확률분포

(python 기초 및 데이터처리)
- Numpy, Pandas, Matplotlib 활용
- OpenCV(영상 처리 기본)
- Scipy(신호 처리 및 회적화)

(기본적인 자율주행 원리 이해)
- 센서 종류 및 역할(LiDAR, 카메라, 레이더, IMU)
- 자율주행 시스템의 구조(Perception -> Planning -> Control)
- CAN 통신 및 차량 제어 기본 개념

## 2. 센서 데이터 처리 및 영상 인식
(OpenCV 기반 영상처리)
- 영상 필터링(Gaussian Blur, Edge Detection)
- 객체 탐지(Contours, Hough Transform)
- 차선 감지(Canny Edge + Hough Transform)

(Deep Learning을 활용한 인식)
- CNN 기본 개념
- Object Detection(YOLO, Faster RCNN)
- 차선 및 신호등 인식(Semantic Segmentation)

(LiDAR 데이터 처리)
- PCL(Point Cloud Library) 기본
- Open3D를 활용한 점군 데이터 시각화

(Sensor Fusion 개념)
- LiDAR + 카메라 결합(Camera-LiDAR Calibration)
- Kalman Filter & Particle Filter 활용(위치 추정 및 객체 추적)

## 3. 주행 알고리즘 구현
(경로 계획: Path Planning)
- Grid-based Search(A*, Dijkstra)
- Sampling-based Planning(RRT, RRT*, PRM)
- Optimal Control(MPC, Dynamic Programming)

(제어 시스템: Control)
- PID 제어(속도 및 조향)
- Pure Pursuit Steering
- Stanley COntroller(고속 차량 제어)

(강화 학습을 활용한 주행)
- OpenAI Gym + CARLA 시뮬레이터 활용
- DQN, PPO 등을 활용한 자율주행 학습

## 4. 시뮬레이터 및 실제 환경 테스트
(자율주행 시뮬레이터 활용)
- CARLA (Python API 지원, 실제 차량 환경과 유사)
- LGSVL (센서 데이터 연동 가능)
- AirSim (드론 및 자율주행 차량 지원)

(ROS & 실제 하드웨어 연동)
- ROS2를 활용한 자율주행 시스템 구축
- Raspberry Pi + Jestson(Nano)을 활용한 실습

(End-to-End 자율주행 구현)
- 센서 데이터를 받아 인식 -> 경로 생성 -> 차량 제어

## Reference
- [MIT 6.S094(2017)](https://github.com/Carmezim/MIT-6.S094)
- [Coursera: Self-Driving Cars Specialization](https://www.coursera.org/specializations/self-driving-cars)
- [Autoware](https://autoware.org/): ROS 기반 오픈소스 자율주행 프로젝트
- [CARLA](https://carla.org/): 오픈소스 자율주행 시뮬레이터
- [DonkeyCar](https://docs.donkeycar.com/): Raspberry Pi 기반 미니 자율주행
- []()

