from PySide2.QtWidgets import QApplication
from controllers.main_window import ListGameWindow


if __name__ == "__main__":
    app = QApplication()
    window = ListGameWindow()
    window.show()
    
    app.exec_()