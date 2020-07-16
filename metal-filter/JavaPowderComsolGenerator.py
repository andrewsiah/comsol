#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:03:13 2020

@author: andrew
"""
import math
import time
#This doc is written with meter as standard metric. 
# 100 micrometer is 0.0001 m
# 1.1mm is 0.0011 m



def generate(r_inner, r_outer, height, r_powder, decimal_place):
    
    """
    Parameters
    ----------
    r_inner : float - distance from center to inner width of circle
    r_outer : float - distance from center to outer width of circle
    height : float - height of metal powder
    r_powder : float - radius of metal powder
    decimal_place : int - number of decimal place of r, theta, and x, y

    Returns
    -------
    A .java file with necessary geoms of metal powder ready 

    """
    
    d_powder = 2*r_powder #distance between 2 powder
    height_count = 0
    
    powder_no = 0 #Keeps count of number of powder produced, and used in naming
    while height_count < height:
        r_count = r_inner
        while r_count <= r_outer:
            theta = angle(d_powder, r_count)
            powder_quantity = (2*math.pi)/theta #quantity of powder per 2pi loop
            powder_count = 0
            theta_count = 0
            while powder_count < powder_quantity:
                #print(powder_no, round(theta_count,decimal_place), round(r_count,decimal_place), round(height_count,decimal_place))
                powder_no += 1
                powder_count += 1
                theta_count += theta
                #converts cylindrical plane to cartesian plane.
                x = r_count * math.cos(theta_count)
                y = r_count * math.sin(theta_count)
                print(powder_no, round(x,decimal_place), round(y,decimal_place), round(height_count,decimal_place))
            r_count += d_powder
        height_count += d_powder
        print("new height!", height_count)
    
    
def angle(d_powder, radius):
    # d_powder = 2*radius*sin(theta/2)
    # theta = 2*arcsin((d_powder)/2*radius)
    return 2*math.asin(d_powder/(2*radius))
    
def printer(x_coor, y_coor, number):
    """
    Description: Prints out the geometry of the powder in java syntax

    """
    
    
    
    return None


start_time = time.time()
generate(0.0011, 0.0014, 0.005, 0.00005,5)
print("--- %s seconds ---" % (time.time() - start_time))