class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def control(self, error, dt=1):
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.prev_error = error
        return output

# PID 값 설정
pid = PIDController(1.0, 0.1, 0.05)

# 주행 테스트
for error in [5, 3, 1, 0, -1, -3, -5]:
    control_value = pid.control(error)
    print(f"Error: {error}, Control Output: {control_value}")
