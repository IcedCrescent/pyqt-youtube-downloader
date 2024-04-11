import sys
from app_window import AppWindow
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = AppWindow()
    main_window.show()
    sys.exit(app.exec())

    