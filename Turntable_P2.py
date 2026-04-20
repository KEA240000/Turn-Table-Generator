import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance

def get_maya_main_win():
    """Return maya main window"""
    main_win_addr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win_addr), QtWidgets.QWidget)

#Create button for the Maya workspace with logo.

class TurnTableWin():
    #create code for the window to open at set size, with proper name, and widgets called.
    def __init__(self):
    #put in intialization code for the window creation.
    def _mk_main_layout(self):
    #Create the main layout of the window.
    def generate_turntable(self):
    #Pass the values of what is input in the GUI to the rest of the code.
    def connect_signals(self):
    #Connect button click signals to do as requested, like close the window.

class TurnTable():
    #Gather the FPS input and place keyframes at the desired points

    #Rotate the object every key frame based on how fast or slow the user wants

    #Export the video file to the desired user location.
