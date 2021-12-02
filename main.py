import sys
from PIL import Image

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

from gui.guiMain import Ui_MainWindow
from gui.E4_DialogUI import Ui_Dialog as E4_Options

from E2_color_to_grey import convert_to_greyscale
from E3_negative import convert_to_negative
from E4_grey_level_slicing import grey_level_slicing
from E5_bit_plane_slicing import convert_to_bit_plane_slicing
from E6_histogram_equalization import histogram_eq, plot_histogram
from E7_contrast_stretching import contrast_stretching

#from handleImageFile import showInputImage, showOutputImage

class E4_Dialog(QDialog, E4_Options):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    

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

        self.actionHistogram_Equalization.triggered.connect(lambda: self.histogramEq())
        self.actionGenerate_Histograms.triggered.connect(lambda: self.plotHistogram())

        self.actionContrast_Stretching.triggered.connect(lambda: self.contrastStretching())

    def openImage(self):
        print("Open Image triggered")
        selectDialog = QFileDialog(self)
        selectDialog.setFileMode(QFileDialog.ExistingFile)
        selectDialog.setNameFilter("Images (*.png *.xpm *.jpg)")
        selectDialog.setDirectory("/home/unity/Documents/Sem7/IP/Practicals/Pics")
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

    def showOutputImage(self, msg=""):
        self.outputPixmap = QPixmap.fromImage(self.outputImage)
        self.outputImageLabel.setPixmap(self.outputPixmap)
        self.msgLabel.setText(msg)
    
    #E2
    def grey(self):
        self.outputImage = convert_to_greyscale(self.inputImagePIL)
        self.showOutputImage()

    #E3
    def negative(self):
        self.outputImage = convert_to_negative(self.inputImagePIL)
        self.showOutputImage()

    #E4
    def greLevelSlicing(self):
        minL, maxL, bg = self.showE4_Dialogue()
        if minL!=-1 and maxL!=-1 and bg!=-1:
            self.outputImage = grey_level_slicing(self.inputImagePIL, minL, maxL, bg)
            bgMsg = ["No", "Yes"][bg] 
            msg = f"Grey Level Slicing : minLevel={minL}, maxLevel={maxL}, retainBackground={bgMsg}"
            self.showOutputImage(msg)

    def showE4_Dialogue(self): 
        dialog = E4_Dialog()
        retValue = dialog.exec_()
        minL, maxL, bg = -1, -1, -1
        if retValue == QDialog.Accepted:
            minL = int(dialog.minLevel.toPlainText())
            maxL = int(dialog.maxLevel.toPlainText())
            bg = int(dialog.bg.toPlainText())
        return minL, maxL, bg

    #E5
    def bitPlane(self, plane):
        self.outputImage = convert_to_bit_plane_slicing(self.inputImagePIL, plane)
        self.showOutputImage()

    #E6
    def histogramEq(self):
        self.outputImage, self.initialHist, self.finalHist = histogram_eq(self.inputImagePIL)
        self.showOutputImage()
    
    def plotHistogram(self):
        plot_histogram(self.initialHist, self.finalHist)

    #E7
    def contrastStretching(self):
        self.outputImage = contrast_stretching(self.inputImagePIL)
        self.showOutputImage("Contrast Stretching")


       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
