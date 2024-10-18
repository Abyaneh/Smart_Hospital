# Smart Hospital


<p align="center">
  <img src="https://github.com/Abyaneh/Smart_Hospital/blob/main/Robotic%20movie%20and%20photos/Structure%20of%20Robot.png" alt="Final_Assembled_Device" width="400"/>
  <img src="https://github.com/Abyaneh/Smart_Hospital/blob/main/Robotic%20movie%20and%20photos/Voice%20assistant%20and%20easy%20to%20use%20in%20the%20bot.png" alt="Final_Assembled_Device" width="400"/>
</p>



## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Layers](#project-layers)
  - [Image Processing Layer](#image-processing-layer)
- [Technologies & Tools Used](#technologies--tools-used)
- [Video Demonstration](#video-demonstration)
- [How to Run the Project](#how-to-run-the-project)
- [Team Members](#team-members)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
This project, developed as part of an introductory robotics course, is an advanced autonomous robot designed to navigate and perform object detection in a hospital environment. The robot follows a path, detects objects such as beds, and interacts with patients through smart functionalities.

---

[Back to Top](#table-of-contents)
## Features
- **Line Following**: The robot follows a black line on the ground using a camera and image processing.
- **Object Detection**: The robot uses Aruco markers and OpenCV to detect and track objects (e.g., patients, beds, and medical equipment) in its vicinity.
- **Smart Curtain Control**: Adjusts room lighting and curtains based on environmental conditions.
- **Voice Assistant**: Interacts with patients by asking health-related questions.
---

[Back to Top](#table-of-contents)
## Project Layers

### Image Processing Layer
As part of the Image Processing Group, I contributed to developing the robot's vision system. Here's a detailed breakdown of the steps we followed:


#### Steps:
1. **Preparation of Images**: We captured digital images using a camera mounted on the robot.
2. **Image Editing**: Modifications were applied to the images to prepare them for processing.
3. **Noise Reduction**: We cleaned the images to remove noise, enhancing clarity.
4. **Color Image Processing**: Performed on both grayscale and RGB images to improve contrast.
5. **Multi-Resolution Processing**: Used to compress large images (e.g., satellite) for real-time use.
6. **Image Compression**: Reduced the image size for faster processing.
7. **Image Segmentation**: Split images into segments to isolate areas of interest (e.g., black path line).
8. **Object Detection**: Implemented using Aruco markers and OpenCV to detect and classify objects such as patients, beds, and medical equipment.

[Back to Top](#table-of-contents)
#### Object Detection in Hallways:
We used **Aruco markers** to assist in object localization, which helped guide the robot. The markers provide accurate tracking and orientation feedback, making them ideal for high-speed real-time applications.


##### Challenges:
- Managing image processing at high speeds caused the robot to veer due to speed discrepancies between motors.
- Tuning the PID controller to adjust motor speeds based on real-time feedback.


[Back to Top](#table-of-contents)
## Technologies & Tools Used
- **OpenCV**: Image processing and path following 
- **Python**: Core language for implementing algorithms 
- **Aruco Markers**: Object detection and tracking 
- **Arduino IDE**: Programming the robot's control system 
- **ESP32**: Microcontroller used for communication and sensor data

---

[Back to Top](#table-of-contents)
## Video Demonstration

#### you can see two videos from the demonstration

Click [here](https://github.com/Abyaneh/Smart_Hospital/blob/main/Robotic%20movie%20and%20photos/functionality_1.mp4) to watch the full video 1 demonstration

Click [here](https://github.com/Abyaneh/Smart_Hospital/blob/main/Robotic%20movie%20and%20photos/functionality_2.mp4) to watch the full video 2 demonstration

---

[Back to Top](#table-of-contents)
## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Abyaneh/Smart_Hospital
   ```
2. Install the dependencies:
    ```bash
    python main.py
    ```
3. Ensure the robot is connected to your computer or microcontroller before running the code.

[Back to Top](#table-of-contents)
## Team Members
- **Image Processing Group:** Mohammad Maleki Abyaneh, Aghazadeh, Elmi, Ghaffarzadeh, Sharifi
- **Curtain and Smart Light Group:** Faraji, Gol Nabi
- **Chassis Design Group:** Rahi Sharafi, Nalbandian
- **Voice Assistant Group:** Pdash and Ershad
- **Motor Team:** Padash, Samieinia


![Image Processing Group](https://github.com/Abyaneh/Smart_Hospital/blob/main/Robotic%20movie%20and%20photos/Image%20Processing%20Group.png)

[Back to Top](#table-of-contents)
## Contributing
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add a new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request for review.

[Back to Top](#table-of-contents)


## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Abyaneh/rotten_and_fresh/blob/main/LICENSE) file for details.

[Back to Top](#table-of-contents)
