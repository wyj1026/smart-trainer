# coding: utf-8

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from .MainWindow import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.viewfinder = QCameraViewfinder()
        self.available_cameras = QCameraInfo.availableCameras()
        self.select_camera(1)

    def select_camera(self, i):
        self.camera = QCamera(self.available_cameras[i])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.error.connect(lambda: self.alert(self.camera.errorString()))
        self.camera.start()

        self.capture = QCameraImageCapture(self.camera)
        self.capture.error.connect(lambda i, e, s: self.alert(s))
        self.capture.imageCaptured.connect(lambda d, i: self.status.showMessage("Image %04d captured" % self.save_seq))

        self.current_camera_name = self.available_cameras[i].description()
        self.save_seq = 0


def start_app():
    app = QApplication(sys.argv)

    # Init the MainWindow
    w = Window()

    # Add the camera widget
    w.ui.verticalLayout.addWidget(w.viewfinder)

    # Show the main window
    w.show()
    sys.exit(app.exec_())
	
if __name__ == "__main__":
	start_app()