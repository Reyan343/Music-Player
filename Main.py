import fnmatch
import sys, os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QFileDialog, QListWidget, QLabel, QMessageBox
)
from pygame import mixer

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QHBoxLayout()
        self.playButton = QPushButton("Play", self)
        self.pauseButton = QPushButton("Pause", self)
        self.openFileButton = QPushButton("Choose", self)
        
        self.songlist = QListWidget()
        
        layout.addWidget(self.playButton)
        layout.addWidget(self.pauseButton)
        layout.addWidget(self.openFileButton)
        
        layout.addWidget(self.songlist)
        
        central_widget.setLayout(layout)
        
        self.openFileButton.clicked.connect(self.chooseFolder)
        self.playButton.clicked.connect(self.playSong)
        
    def chooseFolder(self):
        self.folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
                    
        if self.folder:
            self.songs = [file for file in os.listdir(self.folder) if fnmatch.fnmatch(file, "*.mp3")]
            #print(folder)
            
            self.songlist.clear()
            self.songlist.addItems(self.songs)
        else:
            error_dialog = QWidget.QErrorMessage()
            error_dialog.showMessage('Please select a folder containing music')
            
    def playSong(self):
        self.songToPlay = os.path.join(self.folder, self.songlist.currentItem().text()) # not sure why currentItem doesnt get the location as well
        #self.songLocation = os.path.join(self.folder, self.songToPlay)
        #print(self.songToPlay)
        
        mixer.init()
        
        mixer.music.load(self.songToPlay)
        
        mixer.music.play()
        
        
app = QApplication(sys.argv)
window = Window()

window.show()

app.exec()
