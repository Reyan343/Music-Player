import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QHBoxLayout()
        
        central_widget.setLayout(layout)

app = QApplication(sys.argv)
window = Window()

window.show()

app.exec()
