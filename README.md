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

#### Image Processing in Room:

#### Steps:
1. **Data preparation**:
- We captured digital images using a camera mounted on the robot, which recorded the live feed as it navigated the environment.
2. **Data Preprocessing**:
- Performed noise reduction techniques such as Gaussian blur to remove unwanted noise from the images.
- Resized the images to a standard resolution for consistent processing.
- Converted the color images to grayscale and applied a threshold for binary conversion (black and white).
3. **Image Segmentation**:
- Segmented areas of interest, particularly the black path line, from the surrounding white background using masking techniques.
- Applied contour detection to isolate the largest black area, ensuring the robot focused on the correct path.
  
4. **Center Line Detection**:
- Used image moments to calculate the center of the largest detected contour (black path line).
- Marked this center with a visual white dot to keep track of the robot's alignment with the path.
5. **Path Adjustment**:
-Calculated the robot’s required movement by analyzing the position of the center dot relative to the image frame.
- Defined the "center" range as being between 190 and 290 pixels from the top of the screen (left-right axis in portrait mode).
- Based on this analysis:
   - If the center dot was outside this range, instructions were sent to the motors to rotate either left or right.
   - If the dot was within the center range, the robot continued moving straight.
6. **Error Calculation**:
- Computed an error variable based on the deviation of the center dot from the optimal center range.
- Sent this error data to the PID controller, which adjusted the speed of the motors for smooth turning and movement.

7. **Visualization**:
- For debugging and real-time tracking, we visualized the contours, mask, and main frame, along with the identification circle representing the detected center.

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
