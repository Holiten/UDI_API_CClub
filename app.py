from PySide2 import QtWidgets

"""
QtWidgets.QVBoxLayout() # Layout Vertical
QtWidgets.QLineEdit()   # Case Line edit
QtWidgets.QListWidget() # Case Liste 
"""


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ciné Club")
        self.setup_ui()

    def setup_ui(self):
        # Layout
        self.layout = QtWidgets.QVBoxLayout(self)

        # Creation boutons
        self.led_write = QtWidgets.QLineEdit()
        self.btn_add = QtWidgets.QPushButton("Ajouter un film")
        self.list_movies = QtWidgets.QListWidget()
        self.btn_remove = QtWidgets.QPushButton("supprimer le(s) film(s)")

        # Insertion dans le layout
        self.layout.addWidget(self.led_write)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.list_movies)
        self.layout.addWidget(self.btn_remove)


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
