#Three simple challenges or one complex one 
#-trying to make the user interface more simplified and readable
#-could add a slider for window contols like how big or small it is 
#-color for flowers and possible shade for it

#Custom Maya shelf button and icon & user interface

#Number of intuative/paramters for asset generator (5 to 10) arguments
#- dividers on window horizontal and vertical
#- flower count in front pot
#- color change of pot
#- possible curtain changes?
#- window size in general
#- change the colors of the flowers in the pot

#Challenge features
#- Extra research for UI interface

import maya.cmds as cmds
import random


class SimpleWindowCreator():

    def ui_interface():
        #set up user inputt first then call other commands
        #create windowtab for user imputs
        pass

    def create_window_frame(width, height, depth, frame_thickness=0.2):
        frame = cmds.polyCube(w=width + frame_thickness* 2,
                              h=height + frame_thickness* 2,
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
 
    dividers_test = horizontal_dividers(width=3.0, height=2.0, depth=0.2, count=3.0)
    print(f"Created horz dividers: {horizontal_dividers}")

