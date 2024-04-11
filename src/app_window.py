from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout
class AppWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_components()

    def init_components(self):
        # Set window size
        self.setFixedSize(600, 400)
        
        # load logo image
        self.image_label = QLabel(self)
        logo = QPixmap("resources/imgs/youtube-icon.png")
        self.image_label.setPixmap(logo.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))

        # Title
        self.title_label = QLabel("Youtube Downloader", self)
        self.title_label.setFont(QFont("Arial", 20))

        # Layout
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.image_label,
            alignment= Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        spacer = QWidget()
        self.layout.addWidget(spacer, stretch = 1)
        self.layout.addWidget(self.title_label,
            alignment = Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(self.layout)





