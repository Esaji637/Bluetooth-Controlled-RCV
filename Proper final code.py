import bluetooth
import RPi.GPIO as GPIO
import time
import atexit

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

# Cleanup function for atexit
def cleanup():
    stop_all()
    GPIO.cleanup()
    print("GPIO cleaned up and motors stopped.")

atexit.register(cleanup)

# Movement functions
def move_backward(speed):
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

def move_forward(speed):
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
    # Turn right by running the left motors and stopping/halting right motors
    GPIO.output(IN1_A, GPIO.LOW)  # Right motor 1
    GPIO.output(IN2_A, GPIO.HIGH)  # Right motor 2
    GPIO.output(IN1_B, GPIO.LOW)  # Right motor 1
    GPIO.output(IN2_B, GPIO.HIGH)  # Right motor 2
    motor1_pwm_A.ChangeDutyCycle(speed)  # Control right motor speed
    motor1_pwm_B.ChangeDutyCycle(speed)  # Control right motor speed
    motor2_pwm_A.ChangeDutyCycle(0)  # Stop left motor 1
    motor2_pwm_B.ChangeDutyCycle(0)  # Stop left motor 2


def turn_left(speed):
    # Turn left by running the right motors and stopping/halting left motors
    GPIO.output(IN3_A, GPIO.LOW)  # Left motor 1
    GPIO.output(IN4_A, GPIO.HIGH)  # Left motor 2
    GPIO.output(IN3_B, GPIO.LOW)  # Right motor 1
    GPIO.output(IN4_B, GPIO.HIGH)  # Right motor 2
    motor2_pwm_A.ChangeDutyCycle(speed)  # Control left motor speed
    motor2_pwm_B.ChangeDutyCycle(speed)  # Control left motor speed
    motor1_pwm_A.ChangeDutyCycle(0)  # Stop right motor 1
    motor1_pwm_B.ChangeDutyCycle(0)  # Stop right motor 2


def stop_all():
    motor1_pwm_A.ChangeDutyCycle(0)
    motor2_pwm_A.ChangeDutyCycle(0)
    motor1_pwm_B.ChangeDutyCycle(0)
    motor2_pwm_B.ChangeDutyCycle(0)

# Bluetooth server function
def start_bluetooth_server():
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_socket.bind(("", bluetooth.PORT_ANY))
    server_socket.listen(1)
    print("Waiting for Bluetooth connection...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    try:
        while True:
            data = client_socket.recv(1024).decode("utf-8").strip()
            if not data:
                break
            print(f"Received: {data}")

            if data == "F":
                print("Moving forward...")
                move_forward(50)
            elif data == "B":
                print("Moving backward...")
                move_backward(50)
            elif data == "L":
                print("Turning left...")
                turn_left(50)
            elif data == "R":
                print("Turning right...")
                turn_right(50)
            elif data == "S":
                print("Stopping all...")
                stop_all()
            else:
                print("Unknown command received.")

            client_socket.send("Command executed.".encode("utf-8"))
    except OSError as e:
        print(f"Connection closed: {e}")
    finally:
        stop_all()
        client_socket.close()
        server_socket.close()
        print("Bluetooth server shut down.")

if __name__ == "__main__":
    start_bluetooth_server()
