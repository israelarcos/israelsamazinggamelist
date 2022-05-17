from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
from views.new_game_window import NewGameForm
from db.games import insert_game, select_game_by_id
import shutil
import os


class NewGameWindow(QWidget, NewGameForm):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.addButton.clicked.connect(self.add_game)
        self.selectFileButton.clicked.connect(self.select_file)
        self.cancelButton.clicked.connect(self.close)
    
    def check_inputs(self):
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        duration = self.durationSpinBox.value()
        path = self.filePathLineEdit.text()

        errors_count = 0
        
        if title == "":
            print("Title is mandatory")
            errors_count += 1
        if category == "":
            print("Category is mandatory")
            errors_count +=1
        if duration == 0:
            print("Duration is mandatory")
            errors_count +=1
        if path == "":
            print("You must select a game")
            errors_count +=1
        
        return (errors_count == 0)
            
        
    def add_game(self):
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        duration = self.durationSpinBox.value()
        path = self.filePathLineEdit.text()
        description = self.descriptionTextedit.toPlainText()

        if self.check_inputs():
            new_path = shutil.copy(path, "game_files")
            data = (title, category, duration, new_path, description)
            if insert_game(data):
                self.clean_inputs()
                self.parent.refresh_table_from_child_window()
            else:
                self.filePathLineEdit.setText(new_path)
                self.undo()

    def clean_inputs(self):
        self.titleLineEdit.clear()
        self.categoryLineEdit.clear()
        self.durationSpinBox.setValue(0)
        self.filePathLineEdit.clear()
        self.descriptionTextedit.clear()

    def select_file(self):
        file_path = QFileDialog.getOpenFileName()[0]
        self.filePathLineEdit.setText(file_path)

    def undo(self):
        file_path = self.filePathLineEdit.text()

        if file_path != "":
            os.remove(file_path)



        
