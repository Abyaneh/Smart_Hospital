# Smart Hospital

![Project Overview](insert_image_here.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Layers](#project-layers)
  - [Image Processing Layer](#image-processing-layer)
  - [My Dataset](#my-dataset)
- [Technologies & Tools Used](#technologies--tools-used)
- [Video Demonstration](#video-demonstration)
- [How to Run the Project](#how-to-run-the-project)
- [Team Members](#team-members)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
This project, developed as part of an introductory robotics course, is an advanced autonomous robot designed to navigate and perform object detection in a hospital environment. Using image processing techniques, the robot follows a path, detects objects such as beds, and interacts with patients through smart functionalities.

---

[Back to Top](#table-of-contents)
## Features
- **Line Following and Obstacle Detection**: The robot follows a black line on the ground using a camera and image processing.
- **Object Detection**: The robot uses YOLO to classify objects (e.g., humans, machines) in its vicinity.
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
8. **Object Detection**: Implemented using YOLO and OpenCV to detect and classify objects such as patients, beds, and medical equipment.

[Back to Top](#table-of-contents)
#### Object Detection in Hallways:
We used **Aruco markers** to assist in object localization, which helped guide the robot. The markers provide accurate tracking and orientation feedback, making them ideal for high-speed real-time applications.


##### Challenges:
- Managing image processing at high speeds caused the robot to veer due to speed discrepancies between motors.
- Tuning the PID controller to adjust motor speeds based on real-time feedback.

---


### My Dataset
For the object detection system, we used a custom dataset created using labeled images of hospital objects (e.g., wheelchairs, patients). The dataset was processed using Roboflow to train our YOLO model.

---

[Back to Top](#table-of-contents)
## Technologies & Tools Used
- **OpenCV**: This is for image processing and path following.
- **Python**: Core language for implementing algorithms.
- **YOLOv5**: Object detection.
- **Arduino IDE**: To program the robot's control system.
- **ESP32**: Microcontroller used for communication and sensor data.

---

[Back to Top](#table-of-contents)
## Video Demonstration
![Video Demo](insert_video_here.gif)

[Click here to watch the full video demonstration](link_to_video_here)

---

[Back to Top](#table-of-contents)
## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Abyaneh/Smart_Hospital/blob/main/README.md#how-to-run-the-project
   ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Install the dependencies:
    ```bash
    python main.py
    ```
4. Ensure the robot is connected to your computer or microcontroller before running the code.

[Back to Top](#table-of-contents)
## Team Members
- **Image Processing Group:** Mohammad Maleki Abyaneh, Mr. Aghazadeh, Mr. Elmi, Mr. Ghaffarzadeh, Mr. Sharifi
- **Curtain and Smart Light Group:** Ms. Faraji, Ms. Gol Nabi
- **Chassis Design Group:** Messrs. Rahi Sharafi, Nalbandian
- **Voice Assistant Group:** Reward, Guidance Gentlemen
- **Motor Team:** Mr. Reward, Mr. Samieinia

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
