import fnmatch
import sys, os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QFileDialog, QListWidget, QLabel, QMessageBox
)
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
#from pygame import mixer

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QHBoxLayout()
        self.playButton = QPushButton("Pause Play", self)
        self.playButton.setCheckable(True)
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
        self.pauseButton.clicked.connect(self.pausePlay)
        
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
        
        self.media_url = QUrl.fromLocalFile(self.songToPlay)
        
        self.player = QMediaPlayer()
        
        self.player.setMedia(QMediaContent(self.media_url))
        
        self.player.setVolume(100)
        
        self.player.play()
        print(self.player.state())
    
    def pausePlay(self):
        if self.player.state() == 1:
            self.player.pause()
        else:
            self.player.play()
    
        
app = QApplication(sys.argv)
window = Window()

window.show()

app.exec()
