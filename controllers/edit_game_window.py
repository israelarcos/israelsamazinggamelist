from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
from views.edit_game_window import EditGameForm
from db.games import select_game_by_id, update_game
import re
import os
import shutil
class EditGameWindow(QWidget, EditGameForm):

    def __init__(self, parent=None, _id=None):
        self._id = _id
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.populate_inputs()
        self.selectFileButton.clicked.connect(self.select_file)
        self.editButton.clicked.connect(self.edit_game)


    def populate_inputs(self):
        data = select_game_by_id(self._id)
        
        self.titleLineEdit.setText(data[1])
        self.categoryLineEdit.setText(data[2])
        self.durationSpinBox.setValue(data[3])
        self.playedtimeSpinBox.setValue(data[4])
        self.filePathLineEdit.setText(data[5])
        self.descriptionTextedit.setText(data[6])

    def select_file(self):
        self.old_path = self.filePathLineEdit.text()
        file_path = QFileDialog.getOpenFileName()[0]
        self.filePathLineEdit.setText(file_path)

        print(file_path)

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
        if path == "":
            print("You must select a game")
            errors_count +=1
        
        if errors_count == 0:
            return True

    def edit_game(self):
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        duration = self.durationSpinBox.value()
        playedtime = self.playedtimeSpinBox.value()
        path = self.filePathLineEdit.text()
        description = self.descriptionTextedit.toPlainText()

        data = [title, category, duration, playedtime, path, description]

        if self.check_inputs():
            path_to_check = "game_files\\" + re.split("/|\\\\", path)[-1]
            result = os.path.exists(path_to_check)

            if result == False:
               data[4] = shutil.copy(path, "game_files")
               os.remove(self.old_path)
            
            if update_game(self._id, data):
                self.close()


            

