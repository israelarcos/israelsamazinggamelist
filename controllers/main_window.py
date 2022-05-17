from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from views.main_window import ListGameForm
from db.games import select_all_games, select_game_by_title, select_game_by_category, delete_game
import os

class ListGameWindow(QWidget, ListGameForm):

    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.open_new_button.clicked.connect(self.open_new_game_window)
        self.open_edit_button.clicked.connect(self.open_edit_game_window)
        self.table_config()
        self.populate_table(select_all_games())
        self.populate_combobox()
        self.refreshButton.clicked.connect( lambda: self.populate_table(select_all_games()))
        self.open_game_button.clicked.connect(self.open_game)
        self.searchButton.clicked.connect(self.search)
        self.delete_game_button.clicked.connect(self.remove_game)
    
    def refresh_table_from_child_window(self):
        data = select_all_games()
        self.populate_table(data)
        
    def add_new_game_row(self, data):
        qty_rows = self.listGamesTable.rowCount()
        index_row = qty_rows
        qty_rows += 1
        self.listGamesTable.setRowCount(qty_rows)
   
        for (index_cell, cell) in enumerate(data):
            self.listGamesTable.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        
        self.records_qty()

    def open_new_game_window(self):
        from controllers.new_game_window import NewGameWindow
        window = NewGameWindow(self)
        window.show()

    def open_edit_game_window(self):
        from controllers.edit_game_window import EditGameWindow
        selected_row = self.listGamesTable.selectedItems()

        if selected_row:
            game_id = int(selected_row[0].text())
            window = EditGameWindow(self, game_id)
            window.show()

        self.listGamesTable.clearSelection()
        
       

    def open_game(self):
        selected_row = self.listGamesTable.selectedItems()

        if selected_row:
            path = selected_row[5].text()
            os.startfile(path)
        self.listGamesTable.clearSelection()

    def remove_game(self):
        selected_row = self.listGamesTable.selectedItems()

        if selected_row:
            game_id = int(selected_row[0].text())
            row = selected_row[0].row()

            if delete_game(game_id):
               file_path =  selected_row[5].text()
               self.listGamesTable.removeRow(row)
               os.remove(file_path)
        
        self.records_qty()

    def table_config(self):
        column_headers = ("Game ID", "Title", "Category", "Duration", "Played time", "Path", "Description")
        self.listGamesTable.setColumnCount(len(column_headers))
        self.listGamesTable.setHorizontalHeaderLabels(column_headers)

        self.listGamesTable.setSelectionBehavior(QAbstractItemView.SelectRows)


    def populate_table(self, data):
        self.listGamesTable.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.listGamesTable.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        self.records_qty()
    
    def add_new_game_row(self, data):
        qty_rows = self.listGamesTable.rowCount()
        index_row = qty_rows
        qty_rows += 1
        self.listGamesTable.setRowCount(qty_rows)
   
        for (index_cell, cell) in enumerate(data):
            self.listGamesTable.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        
        self.records_qty()

    def populate_combobox(self):
        cb_options = ("", "Title", "Category")
        self.searchByCombobox.addItems(cb_options)

    def search_game_by_title(self, title):
        data = select_game_by_title(title)

        self.populate_table(data)

    def search_game_by_category(self, category):
        data = select_game_by_category(category)

        self.populate_table(data)

    def search(self):
        option_selected = self.searchByCombobox.currentText()
        parameter = self.parameterLineEdit.text()

        if option_selected == "":
            print("You must select an option")
        else:
            if parameter == "":
                print("You must write what you want to search")
            else:
                if option_selected == "Title":
                    self.search_game_by_title(parameter)
                elif option_selected == "Category":
                    self.search_game_by_category(parameter)
        


    def records_qty(self):
        qty_rows = str(self.listGamesTable.rowCount())
        self.gamesQtyLabel.setText(qty_rows)

        
