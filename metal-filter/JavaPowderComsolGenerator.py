#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:17:00 2020

@author: Andrew
"""

import math
import time
#This doc is written with meter as standard metric. 
# 100 micrometer is 0.0001 m
# 1.1mm is 0.0011 m



def generate(r_inner, r_outer, height, r_powder, decimal_place, file_name):
    
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
    A .txt file with necessary geoms of metal powder ready 
    """
    
    f = open(file_name + ".txt" , "a")
    
    
    d_powder = 2*r_powder #distance between 2 powder
    z = 0
    
    powder_no = 0 #Keeps count of number of powder produced, and used in naming
    while z <= height:
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
                #print(powder_no, round(x,decimal_place), round(y,decimal_place), round(z,decimal_place))
                x_print = "%."
                y_print = "\"%."+decimal_place"f\" %y"
                z_print = "\"%."+str(decimal_place)+"f\" %z"
                printer(x_print,y_print,z_print,powder_count,r_powder,f)
            r_count += d_powder
        z += d_powder
        print("new height!", z)
    
    
def angle(d_powder, radius):
    # d_powder = 2*radius*sin(theta/2)
    # theta = 2*arcsin((d_powder)/2*radius)
    return 2*math.asin(d_powder/(2*radius))
    
def printer(x, y, z, number, r_powder, file):
    """
    Description: Prints out the geometry of the powder in java syntax
    """
    file.write("model.component(\"comp1\").geom(\"geom1\").create(\"sph"+str(number)+"\", \"Sphere\");\n")
    file.write("model.component(\"comp1\").geom(\"geom1\").feature(\"sph"+str(number)+"\").set(\"pos\", new String[]{\""+x+"\", \""+y+"\", \""+z+"\"});\n")
    file.write("model.component(\"comp1\").geom(\"geom1\").feature(\"sph"+str(number)+"\").set(\"r\", \""+str(r_powder)+"\");\n")        
    
    return None


"""
model.component("comp1").geom("geom1").create("sph13", "Sphere");
    model.component("comp1").geom("geom1").feature("sph13").active(false);
    model.component("comp1").geom("geom1").create("sph14", "Sphere");
    model.component("comp1").geom("geom1").feature("sph14").active(false);
    model.component("comp1").geom("geom1").feature("sph14").label("Powder");
    model.component("comp1").geom("geom1").feature("sph14").set("pos", new String[]{"powdRad", "powdRad", "powdRad"});
    model.component("comp1").geom("geom1").feature("sph14").set("r", "powdRad");
"""


    


start_time = time.time()
generate(0.0011, 0.0014, 0.0005, 0.00005,9,"test1")
print("--- %s seconds ---" % (time.time() - start_time))
