import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance

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
        self.setWindowTitle("Turntable Generator")
        self.resize(300, 200)
        self._mk_main_layout()
        self.connect_signals()
    def _mk_main_layout(self):
    #Create the main layout of the window.
        self.main_layout = QtWidgets.QVBoxLayout()

        self.setLayout(self.main_layout)
    def generate_turntable(self):
    #Pass the values of what is input in the GUI to the rest of the code.

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

class TurnTable():
    #Gather the FPS input and place keyframes at the desired points
    FPS = 24
    Seconds = 5
    RPS = .25
    def get_selection(self):
    #Select objects for the generator to turn.
        objects = cmds.ls(selection=True)
        if not objects:
            cmds.warning("Please select your desired meshes to turn.")
            return None
    #Rotate the object every key frame based on how fast or slow the user wants

    #Export the video file to the desired user location.
