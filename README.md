
<h1 align="center"> DSA Project </h1>   
<h2 align="center">Image Compression using Quadtree DataStructure </h2>

### **Project Team**
### [Shwetha Ajay](https://github.com/ShwethaAjay) 
### [Aryan Bhapkar](https://github.com/aaryannb) 
### [Anjana Gupta](https://github.com/anjanag23468)
### [Karan Manikani](https://github.com/Karan-Manikani)


### Table of Contents
**[Project Description](#proj-description)**<br>
**[Pre-requisites](#pre-requisites)**<br>
**[Guide](#guide)**<br>

## Project Description
The project aims to achieve image compression using quadtree data structure. The image is recursively divided into quadrants till it reaches the case where the all the neighbouring quadrants occupy same or similar colour.<br>
<br> Here’s a showreel to understand the working :<br>

![test_gif](https://github.com/anjanag23468/DSA_Project/blob/main/test_gif.gif)
The image can be compressed at various degrees of compression provided by the user.
## Pre-requisites

Pip commands to install the necessary libraries -<br>
**Windows**<br>
Numpy: pip install numpy<br>
PIL: pip install pillow<br>

**MAC OS**<br>
Numpy: pip3 install numpy<br>
PIL: pip3 install pillow<br>

## Guide

Place both files (compress_image.py and GUI.py) in the same folder and then run GUI.py. This should open up a new window as shown below:<br>
![window_png](https://github.com/anjanag23468/DSA_Project/blob/main/Window.png)


**Input file format (Enter your file)**
1. Reads the image file from the specified path. 
2. Path need not be provided if the image is located in the same directory as the code 
3. File extension must be provided (Fig. 2) 
4. Example: C:\Users\XYZ\Desktop\image.jpg 

**Saving the file (Enter new file name):**
1. Saves the image file to the specified path. 
2. Path need not be provided if the image needs to be saved in the same directory as the code; filename should suffice.
3. File extension must be provided (Fig. 2) 
4. Example 1: C:\Users\XYZ\Desktop\image.jpg 
5. Example 2: image.jpg (Image will be saved in the same directory as the code) 

**Threshold**
1. Sets the degree of compression. 
2. Acceptable input range: 0 – 9 
3. Floating-point numbers result in an error