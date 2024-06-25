# Monte Carlo Pi Approximation

This project is a Python application that approximates the value of π (pi) using the Monte Carlo method. It features a simple user interface (UI) created with the Tkinter library and visualization with the Turtle Graphics library.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Screenshots](#screenshots)
- [Explanation](#explanation)
  - [User Interface](#user-interface)
  - [Simulation](#simulation)
  - [Calculations](#calculations)
  - [Mathematical Basis of the Monte Carlo Method](#mathematical-basis-of-the-monte-carlo-method)

## Requirements
- Python 3.x
- Tkinter library
- Turtle Graphics library

## Installation
Clone or download the project:
\`\`\`bash
git clone https://github.com/YusufCelebii/determining_pi_with_MonteCarlo_method
cd monte-carlo-pi
\`\`\`

Install the required libraries:
\`\`\`bash
pip install tkinter turtle
\`\`\`

## Usage
To run the project, follow these steps:

1. Run the `ui.py` file:
\`\`\`bash
python ui.py
\`\`\`
2. When the user interface opens, enter the number of points for the simulation in the `Number of Points` field and the update frequency in the `Update Frequency` field.
3. Click the `Start Simulation` button to start the simulation.
4. The simulation results will be displayed on the screen.

## File Structure
- `ui.py`: This file manages the user interface. It takes user inputs and starts the simulation.
- `calculations.py`: This file performs Monte Carlo calculations and visualization. It includes drawing the circle and square, generating random points, and calculating the value of π.

## Screenshots
### User Interface
![image](https://github.com/YusufCelebii/determining_pi_with_MonteCarlo_method/assets/95516451/bc66518b-eb4a-49a6-88ed-973b878b741c)

This screenshot shows the interface where users can input simulation parameters. Users can specify the number of points and the update frequency.

### Simulation Screen
![image](https://github.com/YusufCelebii/determining_pi_with_MonteCarlo_method/assets/95516451/6fa7ff17-e801-4269-8357-bb934ea98ac4)


This screenshot shows how the points are distributed inside and outside the circle during the simulation. The approximate value of π and the iteration count are displayed at the top.

## Explanation

### User Interface
The user interface allows users to input the number of points and update frequency for the Monte Carlo simulation.

- **Number of Points**: Specifies the number of random points to be used in the simulation. This affects the accuracy of the calculation.
- **Update Frequency**: Specifies how often the value of π is updated during the simulation. A lower value results in more frequent updates.
- **Start Simulation**: Button to start the simulation. When clicked, the `start_simulation` function is called, and the simulation begins.
- **Reset**: Button to reset the simulation. When clicked, user inputs are cleared, and the simulation stops.

### Simulation
During the simulation, random points are generated within a square that contains a circle. Points are:
- **Red**: Points inside the circle.
- **Blue**: Points inside the square but outside the circle.

This visualization allows us to approximate the value of π using the Monte Carlo method. The ratio of the area of the circle to the area of the square is used to calculate the value of π.

### Calculations
Calculations are performed in the `calculations.py` file and involve the following steps:
1. **Drawing the Circle and Square**: The `area` function draws a circle and a square using Turtle Graphics.
2. **Generating Random Points**: The `random_dots` function generates a specified number of random points and checks whether they are inside the circle.
3. **Calculating the Value of π**: The ratio of points inside the circle to the total number of points inside the square is used to calculate π. This ratio is multiplied by 4 to approximate the value of π.
4. **Printing the Results**: The `print_result` function displays the approximate value of π and the iteration count at specified update frequencies.

### Mathematical Basis of the Monte Carlo Method
The Monte Carlo method is a statistical technique that uses random sampling to approximate mathematical problems. In this project, the steps to approximate π using the Monte Carlo method are as follows:

1. **Define the Square and Circle**:
   - A circle is inscribed within a square. The diameter of the circle is equal to the side length of the square.
   - The area of the square is `4r²` and the area of the circle is `πr²`.

2. **Generate Random Points**:
   - Random points are generated within the square. The coordinates of these points are randomly chosen within the range `(-r, r)`.
   - For each point, it is checked whether the point lies inside the circle. A point is inside the circle if its distance from the origin is less than or equal to `r`.

3. **Calculate the Ratio**:
   - The number of points inside the circle (`N_c`) and the total number of points inside the square (`N_t`) are counted.
   - The ratio of points inside the circle to the total number of points is approximately equal to the ratio of the area of the circle to the area of the square: `N_c / N_t ≈ πr² / 4r² = π / 4`.

4. **Approximate the Value of π**:
   - Using the ratio formula, `π ≈ 4 * (N_c / N_t)` is derived.
   - This formula is used to calculate the approximate value of π.

The accuracy of this Monte Carlo simulation improves with an increasing number of random points. Therefore, the simulation parameters (number of points and update frequency) significantly affect the accuracy and performance of the calculation.


