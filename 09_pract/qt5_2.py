# вариант №5
import sys, collections, random, matplotlib.pyplot as plt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QDesktopWidget, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QMainWindow):
    index = 0
    data_len = 100
    figure = plt.figure()
    ax = figure.add_subplot(111)
    plt.rcParams.update({'font.size': 20})
    data = collections.deque(maxlen=data_len)
    for i in range(data_len):
        data.append(0)

    def __init__(self):
        super().__init__()
        uic.loadUi('d2.ui', self)
        self.initUI()
      
    def initUI(self):
        self.center()
        self.setWindowIcon(QIcon('web.png'))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.plot)
        self.timer.start(1000)
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout.insertWidget(0, self.canvas)
        self.plot()
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
        
    def plot(self):
        self.data.append(random.randint(50,60))
        self.ax.clear()
        self.ax.grid()
        self.ax.set_ylim([0,100])
        self.ax.set_xlim([0,100])
        self.ax.set_title('CPU usage', fontsize = 30)
        self.ax.plot(list(self.data), 'g-', linewidth = 3)
        self.canvas.draw()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
