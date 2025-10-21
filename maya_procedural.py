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

    def create_window_frame(width, height, depth, frame_thickness=0.5):
        frame = cmds.polyCube(w=width + frame_thickness * 2,
                              h=height + frame_thickness * 2,
                              d=depth, name="window_frame")[0]
        return frame
    
    windoframe_test = create_window_frame()
    print(windoframe_test)

    def create_glass(width, height, depth):
        glass = cmds.polyCube(w=width, h=height, 
                              d=0.02, name="window_glass")[0]
        cmds.move(0, 0, depth/2 - 0.05, glass)
        return glass
    
    glass_test = create_glass()
    print(glass_test)

    def horizontal_dividers(width, height, depth, count, thickness=0.1)
        pass
    # def window_generation(self):
    #     #- dividers on window horizontal and vertical
    #     #- window size in general
    #     #clear out scene before adding more objects
    #     # get parameters from user from ui
    #     frame = cmds.polyCube(width=2, height=2, 
    #                           depth=1, name="test_frame")[0]
    #     glass = cmds.polyCube(width=1, height=2, depth=1, name="test_glass")[0]
    #     cmds.move(0, 0, 0.5, glass)
    #     return [frame, glass]
    
    # test_onj = window_generation()
    # print("test:", test_onj)


    # def create_curtains(self, width, style, height):
    #     # user input w/ buttons as to if curtauns are opened, straight or wavy
    #     # size of curtains S to L
    #     #  

    # def create_flower_pot(self, numof_flower):

