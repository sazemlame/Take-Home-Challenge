# Take Home Challenge 

This is a very simple list-basedimplementation of an Automated Parking System.This application helps you manage a parking lot of n slots. The program has the following functionalities:
    1. Park a car in empty slot and store the licence plate number and age of the driver
    2. Record which car has left the parking spot and point the indicator to the nearest empty space from the gate
    3. Search for the slot number for a particular licence number and age
    4. Search for licence plate details for drivers of same age

A list of dictionaries containing details for each car has been implemented. A number of constraints have been taken into care like:
    1. The first line of file should create a parking lot. If not, then a prompt is generated
    2. Same car cannot be parked twice. If so, report the issue to the user
    3. The size of parking lot remains fixed as per the initialisation 
    4. Driver cannot be under the age of 18.
    5. The slot which is being vacated cannot be greater than the length of parking lot 
    6. Licence plate number should follow the standard format
The data system applied behind the implementation is a list of dictionaries, each dictionary element containing licence plate number and age of the driver. This restricts the parking to n slots and operation can be performed simply accessing the elements in the list. As this is a file-based system, every time an input file is read a new parking lot is created and the parking lot is removed from memory on successful execution of the commands in the file. Sample input and output files are given in this repository as input.txt and output.txt.



To run this code you would need to enter the name for the input file. The file must in same directory as the program for execution of the system. For any operating system with Python installed on it, the program can be run from the command prompt. If not then the following steps shall be followed to settup python:
    1. For Windows: https://docs.python.org/3.6/using/windows.html
    2. For Linux and MacOS: https://docs.python-guide.org/starting/install3/linux/
For running the code:
    1. For Windows: 
      * Open cmd, type the path of the folder in which the script is situated
      * Type python(or python3) takehome.py
      * Enter the filename
    2. For Linux and MacOS:
      * Open terminal, go to the required directory using cd *dirname/*
      * Type python(or python3) takehome.py
      * Enter the input filename
       
