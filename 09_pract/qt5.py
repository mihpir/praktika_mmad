# вариант №5
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QDesktopWidget, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    images = ['1.png', '2.png', '3.jpg', '4.jpg', '5.jpg',
              '6.jpg', '7.png', '8.jpg', '9.jpg', '10.png']
    index = 0
    def __init__(self):
        super().__init__()
        uic.loadUi('d.ui', self)
        self.btn_left.clicked.connect(self.f_btn_l)
        self.btn_right.clicked.connect(self.f_btn_r)
        self.initUI()
      
    def initUI(self):
        self.center()
        self.setWindowIcon(QIcon('web.png'))
        self.set_pixmap()
        self.show()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Сообщение',
                "Вы уверены, что хотите выйти?", QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes: event.accept()
        else: event.ignore()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def set_pixmap(self):
        pixmap = QPixmap(self.images[self.index])
        self.label.setPixmap(pixmap.scaled(800, 600))
        
    def f_btn_l(self):
        if self.index == 0: self.index = len(self.images)-1
        else: self.index -= 1
        self.set_pixmap()
        
    def f_btn_r(self):
        if self.index == len(self.images)-1: self.index = 0
        else: self.index += 1
        self.set_pixmap()
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
