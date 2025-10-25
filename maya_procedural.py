#Three simple challenges or one complex one 
#-trying to make the user interface more simplified and readable
#-could add a slider for window contols like how big or small it is 

#Custom Maya shelf button and icon & user interface

#Number of intuative/paramters for asset generator (5 to 10) arguments
#- dividers on window horizontal and vertical
#- possible curtain changes?
#- window size in general

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

        if not cmds.onjExists(shader_name):
            shader = cmds.shadingNode('lambert', asShader=True, 
                                      name=shader_name)
            shading_group = cmds.sets(renderable=True, noSurfaceShader=True,
                                      empty=True, name=shading_group)
            cmds.connectAttr(f'{shader}.outColor', 
                             f'{shading_group}.surfaceShader')
            
            color_map = {'White': (1, 1, 1), 'Black': (0, 0, 0), 
                         'Red': (1, 0, 0), 'Green': (0, 1, 0), 
                         'Blue': (0, 0, 1), 'Brown': (0.4, 0.2, 0), 
                         'Gray': (0.5, 0.5, 0.5), 'Dark_blue': (0, 0, 0.5), 
                         'Dark_red': (0.5, 0, 0), 
                         'Light_blue': (0.7, 0.7, 1.0), 'Yellow': (1, 1, 0), 
                         'Purple': (0.5, 0, 0.5)}
            
            rgb = color_map.get(color, (0.5, 0.5, 0.5))
            cmds.setAttr(f'{shader}.color', rgb[0], rgb[1], rgb[2], 
                         type='double3')

            for obj in objects:
                cmds.sets(obj, edit=True, forceElement=shading_group)

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
    def create_dividers_group(width, height, depth, hor_div_count=0, 
                              ver_div_count=0, thickness=0.1):
        dividers = []
        if hor_div_count > 0:
            hor_dividers = SimpleWindowCreator.horizontal_dividers(width, 
                                height, depth, hor_div_count, thickness)
            
            dividers.extend(hor_dividers)

        if ver_div_count > 0:
            ver_dividers = SimpleWindowCreator.vertical_dividers(width, 
                                height, depth, hor_div_count, thickness)
            
            dividers.extend(ver_dividers)

        if dividers:
            dividers_group = cmds.group(dividers, name="window_dividers_grp")
            return dividers_group
        else:
            return None

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
        curtain_thickness = 0.1
        curtain_width = width * 1.2
        curtain_height = height * 1.1
        
        curtain = cmds.polyCube(w=curtain_width,
                              h=curtain_height,
                              d=curtain_thickness, name="closed_curtain")[0]
        
        cmds.move(0, 0, frame_depth/2 + curtain_thickness/2 + 0.05, curtain)

        rod_len = curtain_width * 1.1
        rod_radi = max(0.2, width * 0.007)
        rod = cmds.polyCylinder(r=rod_radi, h=rod_len, name="curtain_rod")[0]
        cmds.rotate(0, 0, 90, rod)
        cmds.move(0, height/2 + 0.1, frame_depth/2 + curtain_thickness + 0.05,
        rod)

        curtain_group = cmds.group(curtain, rod, name="closed_curtains_grp")
        return curtain_group
    
    def create_complete_window(width=3.0, height=2.0, depth=0.2, 
                               hor_div_count=1, ver_div_count=1, 
                               curtain_type='open'):
        frame = SimpleWindowCreator.create_window_frame(width, height, depth)
        glass = SimpleWindowCreator.create_glass(width, height, depth)

        dividers_group = SimpleWindowCreator.create_dividers_group(width, 
                                height, depth, hor_div_count, ver_div_count)

      
    
    # dividers_test = create_closed_curtians(width=3.0, height=2.0, 
    #                                      frame_depth=0.2)
    # print(f"Create left side curtain: {create_closed_curtians}")