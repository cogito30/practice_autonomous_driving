import numpy as np

# 벡터 연산
v1 = np.array([1, 2])
v2 = np.array([3, 4])
dot_product = np.dot(v1, v2)  # 내적 계산
print(f"벡터 내적: {dot_product}")

# 행렬 연산
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(A, B)  # 행렬 곱
print(f"행렬 곱:\n{matrix_product}")

# f(x) = x^2 함수의 기울기를 구하고 경사 하강법 적용
def gradient_descent(x, lr=0.1, epochs=10):
    for _ in range(epochs):
        grad = 2 * x  # f'(x) = 2x
        x -= lr * grad
        print(f"x: {x:.4f}")
    return x

x_init = 5  # 초기값 설정
x_opt = gradient_descent(x_init)
print(f"최적화된 x 값: {x_opt}")