import RPi.GPIO as GPIO
import time

# Motor board 1 pin definitions
IN1_A = 16   # Motor 1 on board 1
IN2_A = 18
ENA_A = 22  # Speed control for motor 1 on board 1

IN3_A = 23  # Motor 2 on board 1
IN4_A = 14
ENB_A = 25  # Speed control for motor 2 on board 1

# Motor board 2 pin definitions
IN1_B = 3   # Motor 1 on board 2
IN2_B = 6
ENA_B = 12  # Speed control for motor 1 on board 2

IN3_B = 26  # Motor 2 on board 2
IN4_B = 13
ENB_B = 19  # Speed control for motor 2 on board 2

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up motor pins as output
GPIO.setup(IN1_A, GPIO.OUT)
GPIO.setup(IN2_A, GPIO.OUT)
GPIO.setup(ENA_A, GPIO.OUT)
GPIO.setup(IN3_A, GPIO.OUT)
GPIO.setup(IN4_A, GPIO.OUT)
GPIO.setup(ENB_A, GPIO.OUT)

GPIO.setup(IN1_B, GPIO.OUT)
GPIO.setup(IN2_B, GPIO.OUT)
GPIO.setup(ENA_B, GPIO.OUT)
GPIO.setup(IN3_B, GPIO.OUT)
GPIO.setup(IN4_B, GPIO.OUT)
GPIO.setup(ENB_B, GPIO.OUT)

# Set up PWM for motor speed control
motor1_pwm_A = GPIO.PWM(ENA_A, 100)  # Board 1, Motor 1
motor2_pwm_A = GPIO.PWM(ENB_A, 100)  # Board 1, Motor 2
motor1_pwm_B = GPIO.PWM(ENA_B, 100)  # Board 2, Motor 1
motor2_pwm_B = GPIO.PWM(ENB_B, 100)  # Board 2, Motor 2

motor1_pwm_A.start(0)  # Start with 0% duty cycle
motor2_pwm_A.start(0)
motor1_pwm_B.start(0)
motor2_pwm_B.start(0)

# Movement functions
def move_forward(speed):
    # Move all motors forward
    GPIO.output(IN1_A, GPIO.HIGH)
    GPIO.output(IN2_A, GPIO.LOW)
    GPIO.output(IN3_A, GPIO.HIGH)
    GPIO.output(IN4_A, GPIO.LOW)
    
    GPIO.output(IN1_B, GPIO.HIGH)
    GPIO.output(IN2_B, GPIO.LOW)
    GPIO.output(IN3_B, GPIO.HIGH)
    GPIO.output(IN4_B, GPIO.LOW)
    
    motor1_pwm_A.ChangeDutyCycle(speed)
    motor2_pwm_A.ChangeDutyCycle(speed)
    motor1_pwm_B.ChangeDutyCycle(speed)
    motor2_pwm_B.ChangeDutyCycle(speed)

def move_backward(speed):
    # Move all motors backward
    GPIO.output(IN1_A, GPIO.LOW)
    GPIO.output(IN2_A, GPIO.HIGH)
    GPIO.output(IN3_A, GPIO.LOW)
    GPIO.output(IN4_A, GPIO.HIGH)
    
    GPIO.output(IN1_B, GPIO.LOW)
    GPIO.output(IN2_B, GPIO.HIGH)
    GPIO.output(IN3_B, GPIO.LOW)
    GPIO.output(IN4_B, GPIO.HIGH)
    
    motor1_pwm_A.ChangeDutyCycle(speed)
    motor2_pwm_A.ChangeDutyCycle(speed)
    motor1_pwm_B.ChangeDutyCycle(speed)
    motor2_pwm_B.ChangeDutyCycle(speed)

def turn_right(speed):
    # Turn right by moving only one side of the motors
    GPIO.output(IN1_A, GPIO.LOW)
    GPIO.output(IN2_A, GPIO.HIGH)
    GPIO.output(IN1_B, GPIO.LOW)
    GPIO.output(IN2_B, GPIO.HIGH)
    
    motor1_pwm_A.ChangeDutyCycle(speed)
    motor1_pwm_B.ChangeDutyCycle(speed)

def turn_left(speed):
    # Turn left by moving only one side of the motors
    GPIO.output(IN3_A, GPIO.LOW)
    GPIO.output(IN4_A, GPIO.HIGH)
    GPIO.output(IN3_B, GPIO.LOW)
    GPIO.output(IN4_B, GPIO.HIGH)
    
    motor2_pwm_A.ChangeDutyCycle(speed)
    motor2_pwm_B.ChangeDutyCycle(speed)

def stop_all():
    # Stop all motors
    motor1_pwm_A.ChangeDutyCycle(0)
    motor2_pwm_A.ChangeDutyCycle(0)
    motor1_pwm_B.ChangeDutyCycle(0)
    motor2_pwm_B.ChangeDutyCycle(0)

try:
    # Move forward for 2 seconds
    print("Moving forward...")
    move_forward(50)
    time.sleep(2)
    
    # Stop motors
    print("Stopping...")
    stop_all()
    time.sleep(1)

    # Move backward for 2 seconds
    print("Moving backward...")
    move_backward(50)
    time.sleep(2)

    # Stop motors
    print("Stopping...")
    stop_all()
    time.sleep(1)

    # Turn right for 2 seconds
    print("Turning right...")
    turn_right(50)
    time.sleep(2)

    # Stop motors
    print("Stopping...")
    stop_all()
    time.sleep(1)

    # Turn left for 2 seconds
    print("Turning left...")
    turn_left(50)
    time.sleep(2)

    # Stop motors
    print("Stopping...")
    stop_all()

finally:
    # Clean up GPIO settings
    motor1_pwm_A.stop()
    motor2_pwm_A.stop()
    motor1_pwm_B.stop()
    motor2_pwm_B.stop()
    GPIO.cleanup()
