# Multidisciplinary Project

## Description

The project addresses the optimization challenge in logistics and packaging industries, focusing on efficiently placing two-dimensional objects within a designated space. The optimization algorithm aims to minimize wasted space, reduce resource usage, and cut additional costs. The project incorporates a three-axis robot for cutting or drawing, enhancing safety and reducing workload in specified areas. 
For photos and more details, read the Report.pdf availaible in this repository.

## Contribution

My primary contribution to this project involved the development of an optimization algorithm and Python code. Specifically:
- Developed an algorithm using the [Hyperpak](https://github.com/AlkiviadisAleiferis/hyperpack) library to solve the optimization problem efficiently.
- Implemented Python code to read input data, execute the optimization process, and generate Gcode.
- Utilized the generated Gcode to instruct a three-axis robot for drawing partitions.

## Algorithm Design

The algorithm design is a critical aspect of the project, aiming to develop optimization software that efficiently arranges two-dimensional objects in a specified area. The chosen algorithm, [Hyperpak](https://github.com/AlkiviadisAleiferis/hyperpack), ensures minimal area coverage by the objects.

### Literature Review
The algorithm design began with a comprehensive literature review, examining various methods to optimize the placement of objects. The [Hyperpak](https://github.com/AlkiviadisAleiferis/hyperpack) algorithm was chosen based on its effectiveness in minimizing wasted space.

### Implementation
The implementation involved coding the optimization software using Arduino Uno and CNC shield technologies. The [Hyperpak](https://github.com/AlkiviadisAleiferis/hyperpack) algorithm was integrated to provide precise pencil movements in the X and Y axes, synchronizing with the stepper motors.

### Testing and Results
Extensive testing was conducted using different data sets, including the Hopper-Turton Test Data Set (Class C). The algorithm's success rates, time spent in the insertion process, and the number of excluded shapes were measured over multiple repetitions. The HyperPack algorithm consistently demonstrated high success rates across various data sets.

### Real-world Application
To validate the algorithm's success in real-world applications, an XY drawing robot was created using Arduino UNO R3 and CNC Shield. The optimization output was converted to Gcode format and successfully executed using the Universal Gcode Sender program. The robot's movements along the axes and the rising and falling movement of the pen were precisely controlled based on the optimization results.

## Robot Design

The design and implementation of the three-axis robot play a crucial role in the success of this project. The robot is tasked with making precise movements to cut or draw labels in a specified area. The design process focuses on integrating a three-axis movement capability and supporting it with optimization algorithms.

### Hardware Components
- **Motors:** Nema 17 stepper motors were selected for controlled movements along the X, Y, and Z axes.
- **Wheel Structure:** A movable wheel structure was preferred for enhanced flexibility and stability.
- **Belt and Pulley System:** GT2-6mm Belt and 20 Teeth GT2 6mm Pulley - 5mm Shaft ensure controlled movements.
- **Materials:** 3D printed parts, M5 safety nuts, 625zz wheels, eccentric nuts (6mm), M4 bolts, and other components were chosen for stability and durability.

### Control System
- **Arduino Uno and CNC Shield:** Motors are connected to the Arduino Uno using jumpers for optimal and controlled movements.
- **Integrated Three-Stage Motor:** Ensures precise control of X, Y, and Z axes for controlled up and down movements.

### Testing and Results
The robot design underwent extensive testing to ensure its efficiency and reliability. Comparative tests were conducted to measure the results of adjustments made to the software code, and improvements were implemented based on the testing outcomes. The design successfully demonstrated its capability to make precise movements necessary for cutting or drawing labels.

## Code Layout


The project directory is organized into two main folders:

1. **hyperpack:** This folder contains the library used for the optimization algorithm, namely HyperPack. It encapsulates the core optimization functionality utilized in the project.

2. **main:** This folder is the primary workspace for the project and consists of the following components:
- **data folder:** Contains input data files that can be modified within the `main.py` script to test different scenarios. The file path is adjustable in the code using the following snippet:

     ```python
     # Input and Output selection
     file_path = "data\\C1_1"
     ```

The data folder also stores the output file, which includes the results such as starting points of the rectangles and their width and length. This file is automatically saved to the data folder after each execution of the code.

   - **main.py:**
     - The main Python script responsible for orchestrating the entire optimization process. It reads input data, applies the HyperPack algorithm for optimization, and generates an output file containing the results.

     ```python
     # Convert solution to G-code and write to file
     gcode_output_file = delimiter.join([file_path, "result.gcode"])
     convert_solution_to_gcode(solution=problem.solution, gcode_file=gcode_output_file, scale_factor=6)
     ```

     The `convert_solution_to_gcode` function converts the optimized solution into G-code, which is essential for controlling the movements of the robotic system. The `scale_factor` parameter allows for the scaling up of the output rectangles' size during the cutting process.


## Acknowledgments
- I would like to extend my sincere appreciation to the students who played a pivotal role in the design and implementation of the three-axis robot for this project. 
- A special acknowledgment goes to the creators and contributors of the [Hyperpak](https://github.com/AlkiviadisAleiferis/hyperpack) optimization algorithm. The project heavily relies on the efficiency and robustness of [Hyperpak](https://github.com/AlkiviadisAleiferis/hyperpack) for solving the package placement problem. We are grateful for the valuable contribution of the [Hyperpak](https://github.com/AlkiviadisAleiferis/hyperpack) library to the field of optimization.

