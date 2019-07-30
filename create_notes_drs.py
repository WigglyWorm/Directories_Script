# Nicola Blackstock
#Assignment 4 Part 1
#Due Date: June 26th 2019
# UCBE Cyber Security 

import os
def main():
     # Create Directory
    dirName = 'CyberSecurity-Notes' 
    try:
    # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")
        
    for subfolder in [
        'Week1','Week2','Week3','Week4',
        'Week5','Week6','Week7','Week8', 
        'Week9','Week10','Week11','Week12', 
        'Week13','Week14','Week15','Week16', 
        'Week17','Week18','Week19','Week20', 
        'Week21','Week22','Week23', 'Week24' ]:
        os.makedirs(os.path.join(dirName, subfolder))
        os.makedirs(os.path.join(dirName, subfolder, 'Day1'))
        os.makedirs(os.path.join(dirName, subfolder, 'Day2'))
        os.makedirs(os.path.join(dirName, subfolder, 'Day3'))  
main()