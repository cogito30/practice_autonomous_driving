# Path Planning

## 학습 목표
- A* 알고리즘: 최단 경로 탐색
- Dijkstra 알고리즘: 비용 기반 최적 경로 탐색
- PID 제어: 차량 속도 및 조향각 조절
- OpenAI Gym 활용한 시뮬레이션

## 1. 최단 경로 탐색 알고리즘
- A*와 Dijkstra로 최적의 경로 탐색
- A* 알고리즘: 경로 탐색 시 휴리스틱(예상 비용) + 실제 이동 비용을 고려하여 빠르게 목적지에 도착하는 알고리즘. 장애물을 우회하는 경로를 빠르게 탐색
- Dijkstra 알고리즘: 최단 거리 탐색. 가장 비용이 적은 경로 탐색

## 2. PID제어 (속도 및 조향각 조절)
- 자율주행에서는 차량의 속도와 방향 제어가 필요
- PID(Proportional-Integral-Derivative) 제어기를 활용하여 정밀 조정

(PID 제어 기본 개념)
- PID는 현재 위치와 목표 위치의 차이를 보정하면서 주행하는 방식
- P(비례 제어): 현재 오차를 기반으로 속도 조절
- I(적분 제어): 지속적인 오차를 보정하여 정밀도 향상
- D(미분 제어): 급격한 변화 방지
=> PID를 활용하여 차선 유지 및 장애물 회피 가능

## 3. OpenAI Gym을 활용한 시뮬레이션 
- gym 설치
```
pip install swig
pip install 'gym[box2d]'
pip install "gymnasium[box2d]"
conda install conda-forge::gym-box2d
```
+) mac에서 설치가 안될시
- [참고](https://j-codingbox.tistory.com/20)
```
brew install cmake boost boost-python sdl2 swig wget
```
- carracing 실행
```
import gym

env = gym.make("CarRacing-v2", render_mode="human")
env.reset()

for _ in range(1000):
    env.render()
    action = env.action_space.sample()  # 랜덤 액션
    env.step(action)

env.close()
```
- 가상환경을 통해 테스트
