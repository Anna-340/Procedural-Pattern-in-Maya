#Three simple challenges or one complex one 
#-trying to make the user interface more simplified and readable
#-could add a slider for window contols like how big or small it is 

#Custom Maya shelf button and icon & user interface

#Number of intuative/paramters for asset generator (5 to 10) arguments
#- dividers on window horizontal and vertical
#- possible curtain changes?
#- window size in general
#- change the colors of the flowers in the pot

#Challenge features
#- Extra research for UI interface

import maya.cmds as cmds
import random


class SimpleWindowCreator():

    def assign_color(objects, color):
        if not isinstance(objects, list):
            objects = [objects]

        shader_name = f"{color}_shader"
        shading_group = f"{color}_SG"

    def ui_interface():
        #set up user inputt first then call other commands
        #create windowtab for user imputs
        pass

    def create_window_frame(width, height, depth, frame_thickness=0.2):
        frame = cmds.polyCube(w=width + frame_thickness * 2,
                              h=height + frame_thickness * 2,
                              d=depth, name="window_frame")[0]
        return frame

    def create_glass(width, height, depth):
        glass = cmds.polyCube(w=width, h=height, 
                              d=0.01, name="window_glass")[0]
        cmds.move(0, 0, depth/2 - 0.05, glass)
        return glass
    
    # window_frame_test = create_window_frame(width=3.0, height=2.0, depth=0.2)
    # print(f"Created Window Frame: {window_frame_test}")

    # glass_test = create_glass(width=2.0, height=1.0, depth=0.2)
    # print(f"Created Window Frame: {glass_test}")


    def horizontal_dividers(width, height, depth, count, thickness=0.1):
        dividers = []
        for hor in range(count):
            div_y = ((hor + 1) * height / (count + 1) - (height / 2)) 
            div = cmds.polyCube(w=width, h=thickness, 
                                d=depth, name=f"horiz_div_{hor+1}")[0]
            cmds.move(0, div_y, depth/2 - depth/2, div)
            dividers.append(div)
        return dividers
 
    # dividers_test = horizontal_dividers(width=3.0, height=2.0, 
    #                                     depth=0.2, count=3)
    # print(f"Created horz dividers: {horizontal_dividers}")

    def vertical_dividers(width, height, depth, count, thickness=0.1):
        dividers = []
        for ver in range(count):
            div_x = ((ver + 1) * height / (count + 1) - (height / 2)) 
            div = cmds.polyCube(w=width, h=thickness, 
                                d=depth, name=f"vert_div_{ver+1}")[0]
            cmds.move(0, div_x, depth/2 - depth/2, div)
            dividers.append(div)
        return dividers

    # dividers_test = vertical_dividers(width=3.0, height=2.0, 
    #                                     depth=0.2, count=3)
    # print(f"Created vert dividers: {vertical_dividers}")

    def create_side_curtains(width, height, frame_depth):
        curtain_thickness = 0.1
        curtain_width = max(0.4, width * 0.015)
        curtain_height = height * 1.3
        curtain_z_pos = frame_depth/2 + curtain_thickness/2 + 0.05

        left_curtain = cmds.polyCube(w=curtain_width, 
                                     h=curtain_height, d=curtain_thickness, 
                                     name="left_curtain")[0]
        cmds.move(-width/2 - curtain_width/2 - 0.05, 0, 
                  curtain_z_pos, left_curtain)
    
        right_curtain = cmds.polyCube(w=curtain_width, h=curtain_height, 
                                      d=curtain_thickness, 
                                      name="right_curtain")[0]
        cmds.move(width/2 + curtain_width/2 + 0.05, 0, 
                  curtain_z_pos, right_curtain)
        
        rod_len = width + curtain_width * 2 + 0.2
        rod_radi = max(0.25, width * 0.008)
        rod = cmds.polyCylinder(r=rod_radi, h=rod_len, name="curtain_rod")[0]
        cmds.rotate(0, 0, 90, rod)
        cmds.move(0, height/2 + 0.15, curtain_z_pos, rod)

        return [left_curtain, right_curtain, rod]
    
    # dividers_test = create_side_curtains(width=3.0, height=2.0, 
    #                                      frame_depth=0.2)
    # print(f"Create left side curtain: {create_side_curtains}")

    def create_closed_curtians(width, height, frame_depth):
        curtain = cmds.polyCube(w=width + frame_depth * 2,
                              h=height + frame_depth * 2,
                              d=frame_depth * 0.5, name="closed_curtain")[0]
        
        cmds.move(0, 0, frame_depth * 0.75, curtain)

        rod_len = width * 1.2
        rod_radi = max(0.2, width * 0.007)
        rod = cmds.polyCylinder(r=rod_radi, h=rod_len, name="curtain_rod")[0]
        cmds.rotate(0, 0, 90, rod)
        cmds.move(0, height/2 + 0.1, frame_depth/2, rod)

        curtain_group = cmds.group(curtain, rod, name="closed_curtains_grp")
        return curtain_group

      
    
    # dividers_test = create_closed_curtians(width=3.0, height=2.0, 
    #                                      frame_depth=0.2)
    # print(f"Create left side curtain: {create_closed_curtians}")