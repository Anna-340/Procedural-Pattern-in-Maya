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
from PySide2 import QtWidgets, QtCore, QtGui


class SimpleWindowCreator(QtWidgets.QWidget):

    def __init__(self):
        super(SimpleWindowCreator, self).__init__()
        self.setWindowTitle("Window Generator")
        self.setFixedSize(300, 500)
        self.window_group = None
        self.ui_interface()

    def ui_interface(self):
        layout = QtWidgets.QVBoxLayout(self)
        self._window_layout(layout)
        self.hor_ver_dividers_forwin(layout)
        color_layout = self.color_for_win_components()
        layout.addLayout(color_layout)
        curtain_layout = self.curtain_type_layout()
        layout.addLayout(curtain_layout)
        self.win_gen_and_clear_btn(layout)

        self.window_color = (0.8, 0.8, 0.9)
        self.divider_color = (0.3, 0.3, 0.3)
        self.curtain_color = (0.7, 0.2, 0.2)
        self.rod_color = (0.4, 0.2, 0.1)

    def win_gen_and_clear_btn(self, layout):
        self.generate_btn = QtWidgets.QPushButton("Generate Window")
        self.generate_btn.clicked.connect(self.create_complete_window_ui)
        layout.addWidget(self.generate_btn)

        self.clear_btn = QtWidgets.QPushButton("Clear Scene")
        self.clear_btn.clicked.connect(self.clear_scene)
        layout.addWidget(self.clear_btn)

    def color_for_win_components(self):
        color_layout = QtWidgets.QVBoxLayout()
        self.window_color_btn = QtWidgets.QPushButton("Window Color")
        self.window_color_btn.clicked.connect(lambda: 
                                              self.pick_color("window"))
        color_layout.addWidget(self.window_color_btn)
        self.divider_color_btn = QtWidgets.QPushButton("Divider Color")
        self.divider_color_btn.clicked.connect(lambda: 
                                              self.pick_color("divider"))
        color_layout.addWidget(self.divider_color_btn)
        self.curtain_color_btn = QtWidgets.QPushButton("Curtain Color")
        self.curtain_color_btn.clicked.connect(lambda: 
                                              self.pick_color("curtain"))
        color_layout.addWidget(self.curtain_color_btn)
        self.rod_color_btn = QtWidgets.QPushButton("Rod Color")
        self.rod_color_btn.clicked.connect(lambda: 
                                              self.pick_color("rod"))
        color_layout.addWidget(self.rod_color_btn)
        return color_layout

    def curtain_type_layout(self):
        curtain_layout = QtWidgets.QVBoxLayout()
        self.curtain_check = QtWidgets.QCheckBox("Add Curtains")
        self.curtain_check.setChecked(True)
        curtain_layout.addWidget(self.curtain_check)

        curtain_type_layout = QtWidgets.QHBoxLayout()
        curtain_type_layout.addWidget(QtWidgets.QLabel("Curtain Type:"))
        self.curtain_type = QtWidgets.QComboBox()
        self.curtain_type.addItem("Side Curtains")
        self.curtain_type.addItem("Simple Drapes")
        self.curtain_type.addItem("Closed Curtains")
        curtain_type_layout.addWidget(self.curtain_type)
        curtain_layout.addLayout(curtain_type_layout)
        return curtain_layout

    def hor_ver_dividers_forwin(self, layout):
        divider_layout = QtWidgets.QHBoxLayout()
        divider_layout.addWidget(QtWidgets.QLabel("Horiz Dividers:"))
        self.horiz_dividers = QtWidgets.QSpinBox()
        self.horiz_dividers.setValue(1)
        self.horiz_dividers.setRange(0, 5)
        divider_layout.addWidget(self.horiz_dividers)

        divider_layout.addWidget((QtWidgets.QLabel("Vert Dividers:")))
        self.vert_dividers = QtWidgets.QSpinBox()
        self.vert_dividers.setValue(1)
        self.vert_dividers.setRange(0, 5)
        divider_layout.addWidget(self.vert_dividers)
        layout.addLayout(divider_layout)

    def _window_layout(self, layout):
        size_layout = QtWidgets.QHBoxLayout()
        size_layout.addWidget(QtWidgets.QLabel("Width:"))
        self.width_input = QtWidgets.QDoubleSpinBox()
        self.width_input.setValue(3.0)
        self.width_input.setRange(1.0, 10.0)
        size_layout.addWidget(self.width_input)

        size_layout.addWidget(QtWidgets.QLabel("Height:"))
        self.height_input = QtWidgets.QDoubleSpinBox()
        self.height_input.setValue(2.0)
        self.height_input.setRange(1.0, 10.0)
        size_layout.addWidget(self.height_input)
        layout.addLayout(size_layout)

    def pick_color(self, color_type):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            rgb = (color.redF(), color.greenF(), color.blueF())
            if color_type == "window":
                self.window_color = rgb
            elif color_type == "divider":
                self.divider_color = rgb
            elif color_type == "curtain":
                self.curtain_color = rgb
            elif color_type == "rod":
                self.rod_color = rgb

    def assign_color(self, objects, color):
        if not isinstance(objects, list):
            objects = [objects]
        shader_name = f"{color}_shader"
        self.shaders_to_win_components(color, shader_name, objects)

    def shaders_to_win_components(self, objects, color, shader_name):
        shading_group = f"{color}_SG"
        if not cmds.objExists(shader_name):
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

    def create_shader(self, name, color):
        shader = cmds.shadingNode('lambert', asShader=True, name=name)
        sg = cmds.sets(name=name + "SG", empty=True, renderable=True, 
                       noSurfaceShader=True)
        cmds.connectAttr(shader + '.outColor', sg + '.surfaceShader')
        cmds.setAttr(shader + '.color', color[0], color[1], color[2], 
                     type='double3')
        return sg

    def create_window_frame(self, width, height, depth, frame_thickness=0.2):
        frame = cmds.polyCube(w=width + frame_thickness * 2,
                              h=height + frame_thickness * 2,
                              d=depth, name="window_frame")[0]
        cmds.move(0, 0, -depth/2, frame)
        return frame

    def create_glass(self, width, height, depth):
        glass = cmds.polyCube(w=width, h=height, 
                              d=0.01, name="window_glass")[0]
        cmds.move(0, 0, depth/2, glass)
        return glass

    def horizontal_dividers(self, width, height, depth, count, thickness=0.1):
        dividers = []
        for hor in range(count):
            div_y = ((hor + 1) * height / (count + 1) - (height / 2))
            div = cmds.polyCube(w=width, h=thickness, 
                                d=depth, name=f"horiz_div_{hor+1}")[0]
            cmds.move(0, div_y, 0.085, div)
            dividers.append(div)
        return dividers
 
    def vertical_dividers(self, width, height, depth, count, thickness=0.1):
        dividers = []
        for ver in range(count):
            div_x = ((ver + 1) * width / (count + 1) - (width / 2)) 
            div = cmds.polyCube(w=thickness, h=height, 
                                d=depth, name=f"vert_div_{ver+1}")[0]
            cmds.move(div_x, 0, 0.085, div)
            dividers.append(div)
        return dividers

    def create_dividers_group(self, width, height, depth, hor_div_count=0, 
                              ver_div_count=0, thickness=0.1):
        dividers = []
        if hor_div_count > 0:
            hor_dividers = self.horizontal_dividers(width, 
                                height, depth, hor_div_count, thickness)
            
            dividers.extend(hor_dividers)

        if ver_div_count > 0:
            ver_dividers = self.vertical_dividers(width, 
                                height, depth, ver_div_count, thickness)
            
            dividers.extend(ver_dividers)

        if dividers:
            dividers_group = cmds.group(dividers, name="window_dividers_grp")
            return dividers_group
        else:
            return None

    def create_side_curtains(self, width, height, frame_depth):
        curtain_thickness = 0.1
        curtain_width = max(0.4, width * 0.15)
        curtain_height = height * 1.3
        curtain_z_pos = frame_depth/2 + curtain_thickness/2 + 0.1

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
        rod_radi = max(0.04, width * 0.012)
        rod = cmds.polyCylinder(r=rod_radi, h=rod_len, name="curtain_rod")[0]
        cmds.rotate(0, 0, 90, rod)
        cmds.move(0, height/2 + 0.15, curtain_z_pos, rod)

        curtains_group = cmds.group([left_curtain, right_curtain, rod],
                                    name="side_curtains_grp")
        return curtains_group
    
    def create_drapes(self, width, height, frame_depth):
        drape_thickness = 0.08
        drape_width = max(0.35, width * 0.12)
        drape_height = height *1.3

        drape_z_pos = frame_depth/2 + drape_thickness/2 + 0.03
        left_drape = cmds.polyCube(w=drape_width, h=drape_height, 
                                   d=drape_thickness, name="left_drape")[0]
        cmds.move(-width/3, -drape_height/2 + height/2 + 0.1, drape_z_pos, 
                  left_drape)
    
        right_drape = cmds.polyCube(w=drape_width, h=drape_height, 
                                   d=drape_thickness, name="right_drape")[0]
        cmds.move(width/3, -drape_height/2 + height/2 + 0.1, drape_z_pos, 
                  right_drape)
        
        rod_len = width * 0.7
        rod_radius = max(0.035, width * 0.01)
        rod = cmds.polyCylinder(r=rod_radius, h=rod_len, name="drape_rod")[0]
        cmds.rotate(0, 0, 90, rod)
        cmds.move(0, height/2 + 0.1, drape_z_pos, rod)

        drapes_grp = cmds.group([left_drape, right_drape, rod], 
                                name="simple_drapes_grp")
        return drapes_grp

    def create_closed_curtains(self, width, height, frame_depth):
        curtain_thickness = 0.1
        curtain_width = width * 1.2
        curtain_height = height * 1.1
        
        curtain = cmds.polyCube(w=curtain_width,
                              h=curtain_height,
                              d=curtain_thickness, name="closed_curtain")[0]
        
        cmds.move(0, 0, frame_depth + curtain_thickness/2 + 0.1, curtain)

        rod_len = curtain_width * 1.1
        rod_radi = max(0.035, width * 0.01)
        rod = cmds.polyCylinder(r=rod_radi, h=rod_len, name="curtain_rod")[0]
        cmds.rotate(0, 0, 90, rod)
        cmds.move(0, height/2 + 0.1, frame_depth/2 + curtain_thickness + 0.05,
        rod)

        curtain_group = cmds.group(curtain, rod, name="closed_curtains_grp")
        return curtain_group
    
    def create_complete_window(self, width=3.0, height=2.0, depth=0.2, 
                               hor_div_count=1, ver_div_count=1, 
                               curtain_type='Side Curtains'):

        frame = self.create_window_frame(width, height, depth)
        glass = self.create_glass(width, height, depth)

        dividers_group = self.create_dividers_group(width, height, depth, 
                                                hor_div_count, ver_div_count)
        curtains = None
        if curtain_type == "Side Curtains":
            curtains = self.create_side_curtains(width, height, depth)
        elif curtain_type == "Simple Drapes":
            curtains = self.create_drapes(width, height, depth)
        elif curtain_type == "Closed Curtains":
            curtain_type = self.create_closed_curtains(width, height, depth)

        window_parts = [frame, glass]
        if dividers_group:
            window_parts.append(dividers_group)
        if curtains:
            window_parts.append(curtains)

        window_group = cmds.group(window_parts, name="window_group")

        return {'group': window_group, 'frame': frame, 'glass': glass, 
                'dividers_group': dividers_group, 'curtains': curtains}

    def create_complete_window_ui(self):
        width = self.width_input.value()
        height = self.height_input.value()
        hor_div_count = self.horiz_dividers.value()
        ver_div_count = self.vert_dividers.value()
        curtain_type = self.curtain_type.currentText()
        add_curtains = self.curtain_check.isChecked()

        window_data = self.create_complete_window(width=width, height=height,
                                                  hor_div_count=hor_div_count, 
                                                  ver_div_count=ver_div_count,
                        curtain_type=curtain_type if add_curtains else None)
        frame_sg = self.create_shader("frame_shader", self.window_color)
        glass_sg = self.create_shader("glass_shader", (0.9, 0.95, 1.0))
        divider_sg = self.create_shader("divider_shader", self.divider_color)
        curtain_sg = self.create_shader("curtain_shader", self.curtain_color)
        rod_sg = self.create_shader("rod_shader", self.rod_color)

        cmds.sets(window_data['frame'], forceElement=frame_sg)
        cmds.sets(window_data['glass'], forceElement=glass_sg)

        if window_data['dividers_group']:
            divider_children = cmds.listRelatives(window_data['dividers_group'], 
                                                  children=True) or []
            for divider in divider_children:
                cmds.sets(divider, forceElement=divider_sg)

        if window_data['curtains'] and add_curtains:
            curtain_children = cmds.ListRelatives(window_data["curtains"], 
                                            children=True, fullPath=True) or []
            for child in curtain_children:
                child_name = child.split('|')[-1].lower()
                if 'rod' in child_name:
                    cmds.sets(child, forceElement=rod_sg)
                elif any(keyword in child_name for keyword in ['curtain', 'drape']):
                    cmds.sets(child, forceElement=curtain_sg)
        cmds.select(window_data['group'])
        print("Window Created!")
        return window_data
    
    def clear_scene(self):
        window_groups = cmds.ls("window_group*", "side_curtains_grp", 
                                "closed_curtains_grp", "simple_drapes_grp", 
                                "window_dividers_grp", transforms=True)
        if window_groups:
            cmds.delete(window_groups)
            print("Scene Cleared")


if __name__ == "__main__":
    try:
        window_creator.close()
        window_creator.deleteLater()
    except:
        pass
    window_creator = SimpleWindowCreator()
    window_creator.show()