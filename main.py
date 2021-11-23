import sys
from PIL import Image

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

from gui.guiMain import Ui_MainWindow
from gui.E4_DialogUI import Ui_Dialog

from E2_color_to_grey import convert_to_greyscale
from E3_negative import convert_to_negative
from E5_bit_plane_slicing import convert_to_bit_plane_slicing

#from handleImageFile import showInputImage, showOutputImage

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.outputImage = None #ImageQt object
        self.inputImagePIL = None # PIL.Image object

        self.actionOpen.triggered.connect(lambda : self.openImage())
        self.actionSave.triggered.connect(lambda: self.saveImage())
        self.actionRGB_to_Grey.triggered.connect(lambda: self.grey())
        self.actionNegative.triggered.connect(lambda: self.negative())
        
        self.actionGrey_Level_Slicing.triggered.connect(lambda: self.greLevelSlicing())

        self.actionBit_Plane_0.triggered.connect(lambda: self.bitPlane(0))
        self.actionBit_Plane_1.triggered.connect(lambda: self.bitPlane(1))
        self.actionBit_Plane_2.triggered.connect(lambda: self.bitPlane(2))
        self.actionBit_Plane_3.triggered.connect(lambda: self.bitPlane(3))
        self.actionBit_Plane_4.triggered.connect(lambda: self.bitPlane(4))
        self.actionBit_Plane_5.triggered.connect(lambda: self.bitPlane(5))
        self.actionBit_Plane_6.triggered.connect(lambda: self.bitPlane(6))
        self.actionBit_Plane_7.triggered.connect(lambda: self.bitPlane(7))

    def openImage(self):
        print("Open Image triggered")
        selectDialog = QFileDialog(self)
        selectDialog.setFileMode(QFileDialog.ExistingFile)
        selectDialog.setNameFilter("Images (*.png *.xpm *.jpg)")
        if selectDialog.exec_():
            self.inputImagePath = selectDialog.selectedFiles()[0]
            self.inputImagePIL = Image.open(self.inputImagePath)
            self.showInputImage()
    
    def saveImage(self):
        saveDialog = QFileDialog(self)
        saveDialog.setFileMode(QFileDialog.AnyFile)
        saveDialog.setNameFilter("Images (*.png *.xpm *.jpg)")
        name = saveDialog.getSaveFileName(self, 'Save File')[0]
        self.outputPixmap.save(name)

    def showInputImage(self):
        pixmap = QPixmap(self.inputImagePath)
        self.inputImageLabel.setPixmap(pixmap)

    def showOutputImage(self):
        self.outputPixmap = QPixmap.fromImage(self.outputImage)
        self.outputImageLabel.setPixmap(self.outputPixmap)
    
    def grey(self):
        self.outputImage = convert_to_greyscale(self.inputImagePIL)
        self.showOutputImage()

    def negative(self):
        self.outputImage = convert_to_negative(self.inputImagePIL)
        self.showOutputImage()

    def bitPlane(self, plane):
        self.outputImage = convert_to_bit_plane_slicing(self.inputImagePIL, plane)
        self.showOutputImage()

    def greLevelSlicing(self):
        dialog = Ui_Dialog()
        dialog.exec_()
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
