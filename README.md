# Philippines Province Visualizer

## Context
The "Philippines Province Visualizer" is a Python program that allows users to interactively learn about the provinces of the Philippines. This was made using Tkinter and Pandas.

## Prerequisites
Install dependencies   
```bash
    pip install pandas
```
```bash
    pip install playsound
```

## Usage
1. Clone this repository to your local machine:
```bash
   git clone https://github.com/fynn07/philippines-province-visualizer.git
```
2. Navigate to the project directory:
```bash
   cd ph-states-game
```
3. Run the Python script:
```bash
   python main.py
```

## How it works
1. The program will display an interactive map of the Philippines using the bult in Turtle module.
2. The user will be prompted to input the name of a province.
3. If the input matches a province name in the dataset, the program will plot the name of the province on the map at its respective location.
4. If the input does not match any province name, the user will be prompted to enter another name.

## Data Source
The dataset was created by me using an automation tool that was written in Python that would provide the X and Y locations of the province through the click of a button. The 
name of the provinces were processed manually.

## Disclaimer
This program is for educational and illustrative purposes only. The geographical data used in this program may not be up-to-date or completely accurate. Please use reliable sources for accurate geographical information. The author of this program shall not be held responsible for any misuse or misrepresentation of the data.