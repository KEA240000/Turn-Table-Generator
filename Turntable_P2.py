import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance
import os


def get_maya_main_win():
    """Return maya main window"""
    main_win_addr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win_addr), QtWidgets.QWidget)

#Create button for the Maya workspace with logo.


class TurnTableWin(QtWidgets.QDialog):
    #create code for the window to open at set size, with proper name, and widgets called.
    
        
    def __init__(self):
        #put in intialization code for the window creation.
        super().__init__(parent=get_maya_main_win())
        self.turntable = TurnTable()
        self.setWindowTitle("Turntable Generator")
        self.setWindowFlags(QtCore.Qt.Tool) #stablizes it for mac users.
        self.resize(300, 200)
        self._mk_main_layout()
        self.connect_signals()
    def _mk_main_layout(self):
        #Create the main layout of the window.
        self.main_layout = QtWidgets.QVBoxLayout()
        self.turntable_options()
        self.mk_buttons()
        self.setLayout(self.main_layout)
    def generate_turntable(self):
             #Create the turntable based on the user input.
        self.turntable.FPS = self.fps_input.value()
        self.turntable.Seconds = self.seconds_input.value()
        self.turntable.RPS = self.rps_input.value()
        self.turntable.Preset_Lights = self.preset_lights_checkbox.isChecked()
        self.turntable.create_turntable()
    
    def connect_signals(self):
        #Connect button click signals to do as requested, like close the window.
        self.build_btn.clicked.connect(self.generate_turntable)
        self.cancel_btn.clicked.connect(self.close)

    def mk_buttons(self):
        #Create a generate a close button for the GUI.
        self.build_btn = QtWidgets.QPushButton("Generate")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")
        self.main_layout.addWidget(self.build_btn)
        self.main_layout.addWidget(self.cancel_btn)

    def turntable_options(self):
        #Create the buttons for the user to place values.
        self.fps_label = QtWidgets.QLabel("FPS:")
        self.fps_input = QtWidgets.QSpinBox()
        self.fps_input.setRange(12, 36)
        self.seconds_label = QtWidgets.QLabel("Seconds:")
        self.seconds_input = QtWidgets.QSpinBox()
        self.seconds_input.setRange(5, 30)
        self.rps_label = QtWidgets.QLabel("RPS:")
        self.rps_input = QtWidgets.QDoubleSpinBox()
        self.rps_input.setRange(0.1, 1.0)
        self.preset_lights_checkbox = QtWidgets.QCheckBox("Preset Lights")
        self.main_layout.addWidget(self.fps_label)
        self.main_layout.addWidget(self.fps_input)
        self.main_layout.addWidget(self.seconds_label)
        self.main_layout.addWidget(self.seconds_input)
        self.main_layout.addWidget(self.rps_label)
        self.main_layout.addWidget(self.rps_input)
        self.main_layout.addWidget(self.preset_lights_checkbox)

class TurnTable():
    #Gather the FPS input and place keyframes at the desired points
    FPS = 24
    Seconds = 5
    RPS = .25
    Preset_Lights = True
    def get_selection(self):
        #Select objects for the generator to turn.
        objects = cmds.ls(selection=True)
        if not objects:
            print("Please select your desired meshes to turn.")
            return None
        return objects
    def change_pivots(self, objects):
        #Change the pivots to the center of world.
        for x in objects:
            cmds.xform(x, centerPivots=True)
    def set_lights(self):
        #Place lights if the option is checked.
        if self.Preset_Lights == True:
            cmds.directionalLight(rotation=(45, 4, 0), intensity=0.8)
            cmds.directionalLight(rotation=(-45, -45, 0), intensity=0.8)
    
    def set_keys(self, objects):
        #Rotate the object every key frame based on how fast or slow the user wants.
        total_frames = int(self.FPS * self.Seconds)
        for x in objects:
            for frame in range(total_frames + 1):
                rotation = (frame / self.FPS) * self.RPS * 360
                cmds.setKeyframe(x, attribute='rotateY', t=frame, v=rotation)
            cmds.keyTangent(x, attribute='rotateY', inTangentType='linear', outTangentType='linear')
            cmds.setInfinity(x, attribute='rotateY', postInfinite='cycle')
    def show_video(self):
        #Open the play blast video window
        cmds.playblast(viewer=True)

        
        
    
    def create_turntable(self):
        objects = self.get_selection()
        if not objects:
            return "No objects selected."
        self.change_pivots(objects)
        self.set_lights()
        self.set_keys(objects)
        self.show_video()