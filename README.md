# Bluetooth-Controlled RCV (Remotely Controlled Vehicle)

This project presents a Bluetooth-controlled robotic vehicle (RCV) built using a Raspberry Pi. The RCV is capable of receiving directional commands via a custom MIT App Inventor mobile application, and it features live video streaming and image capture using a Raspberry Pi camera module. The goal was to create a reliable, responsive, and portable RCV suitable for short-range applications, with a focus on modular design and future extensibility.

The system integrates GPIO-based motor control via L298N motor driver boards, Bluetooth communication for wireless command input, and real-time camera feedback. The project aims to serve as a foundation for future development in remote-controlled systems operating in hazardous or constrained environments.

**The attached link is to view the Live Video Streaming of the Raspberry Pi Camera**: https://www.youtube.com/shorts/BYkzvP-pS94

**The attached link is to view the movement of the RCV using the custom built mobile app**: 
https://www.youtube.com/watch?v=1j99lfryHSs


## 📂 Repository Contents

| File Name                  | Description |
|---------------------------|-------------|
| `Proper final code.py`    | Main integrated script handling Bluetooth commands, motor control, and camera operations. |
| `Bluetooth Testing Code.py` | Script for testing Bluetooth communication and serial input parsing. |
| `Motor Testing Code.py`   | Verifies motor direction and speed control using GPIO and PWM logic. |
| `camera module code.py`   | Handles camera preview, image capture, and streaming setup. |
| `README.md`               |  Overview of the project and how to use it.

---

## Setup Instructions

1. **Hardware Requirements**:
   - Raspberry Pi 4B (or equivalent)
   - L298N motor driver boards ×2
   - TT Gear Motors ×4
   - Pi Camera Module
   - 5V power supply + 9.6V motor power source
   - MIT App Inventor mobile app (custom-made for this project)

2. **Software Requirements**:
   - Raspbian OS
   - Python 3
   - Required libraries: `RPi.GPIO`, `time`, `os`, `socket`, `cv2`, `picamera2`, `pybluez`

3. **Enable Camera and Bluetooth**:
   ```bash
   sudo raspi-config


---

## SSH Access via VS Code

You can write and test code on the Raspberry Pi remotely using Visual Studio Code with SSH.

### Steps:

1. **Enable SSH on the Raspberry Pi**  
   Open a terminal on the Pi and run:
   ```bash
   sudo raspi-config
   
2. **Navigate to**
Interface Options > SSH > Enable
Install "Remote - SSH" extension in VS Code

3. Open VS Code on your computer.
Go to the Extensions tab (or press Ctrl+Shift+X).
Search for and install: Remote - SSH by Microsoft.

4. Connect to the Raspberry Pi
Press Ctrl+Shift+P and type:
makefile
Copy
Edit
Remote-SSH: Connect to Host...
Enter your Pi's IP address in the format:
**pi@192.168.x.x**
When prompted, enter the password for your Pi (default is raspberry if not changed).

5. Start coding remotely!
VS Code will open a new window connected to your Pi. You can now write, edit, and run code on the Raspberry Pi as if it were a local project.



**How to Run the Code (Simple Walkthrough)**
Follow these steps to get the project up and running:
1. **Connect all hardware**: Make sure your motors, motor drivers, Raspberry Pi, camera, and power supplies are properly wired.
2. **Power up the Pi**: Boot into Raspberry Pi OS.
3. **Open the terminal** and navigate to the project folder:
   ```bash
   cd ~/Bluetooth-Controlled-RCV
4. **Run the main script** which is below
python3 "Proper final code.py"



**Acessing MIT App Inventor**
This is the link to access the MIT App Inventor: https://ai2.appinventor.mit.edu/#5850147641688064 you can edit this file with the app components and the logic inside it.
![image](https://github.com/user-attachments/assets/b00172d7-1c3e-4747-ac78-96361a851609)
The QR Code is to access and Download the app onto your phone. 



**Technical Details**
Motor control is handled using PWM signals sent via the Raspberry Pi’s GPIO pins. The L298N drivers interpret those signals to control motor speed and direction.

Bluetooth communication uses the **pybluez** library, which allows the Pi to act as a Bluetooth server, listening for single-character commands from the app.

Camera functionality uses the **picamera2** and **OpenCV** libraries for image capture and **MJPEG** streaming.

Latency measurements were gathered using stopwatch-based testing. Motion command latency averaged ~130–140 ms, while camera-related commands were slightly higher (~160–180 ms).

Power system was designed to supply approximately 6.5–7 W during peak use, divided between the motors and Raspberry Pi.

No complex equations were used, but digital signal timings (e.g., PWM duty cycles) were tuned manually for motor behaviour.

**The following link will help with Camera Live stream**: https://pimylifeup.com/raspberry-pi-webcam-server/

**The following link will helo with setting up Bluetooth on Raspberry Pi**: https://www.youtube.com/watch?v=sY06F_sPef4

**The following link will help with Raspberry Pi setup, hardware and software**: https://www.raspberrypi.com/documentation/


**Known Issues and Future Improvements**
Bluetooth range is limited (~10–15 m indoors). Replacing it with Wi-Fi would allow more flexible control and longer range.

Camera quality drops in low light, resulting in blur or lower FPS.

No autonomous functionality yet — adding AI or obstacle detection with A* pathfinding would improve navigation.

App is only available for Android — future work could involve converting to a web-based control interface.

No feedback from sensors — adding IR, ultrasonic, or GPS modules could enhance RCV awareness and autonomy.

Chassis is basic — a waterproof or shock-resistant enclosure could make the buggy suitable for real-world harsh environments.


