from PySide2 import QtWidgets, QtCore
from movies import get_movies_instance, Movie

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
        self.populate_movies()
        self.setup_connection()

    def setup_ui(self):
        # Layout
        self.layout = QtWidgets.QVBoxLayout(self)

        # Creation boutons
        self.led_write = QtWidgets.QLineEdit()
        self.btn_add = QtWidgets.QPushButton("Ajouter un film")
        self.list_movies = QtWidgets.QListWidget()
        self.list_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_remove = QtWidgets.QPushButton("supprimer le(s) film(s)")

        # Insertion dans le layout
        self.layout.addWidget(self.led_write)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.list_movies)
        self.layout.addWidget(self.btn_remove)

    def setup_connection(self):
        # Gestion des connections
        self.btn_add.clicked.connect(self.add_movie)
        self.btn_remove.clicked.connect(self.remove_movies)
        self.led_write.returnPressed.connect(self.add_movie)

    def populate_movies(self):
        movies = get_movies_instance()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)  # Attacher l'item
            self.list_movies.addItem(lw_item)

    def add_movie(self):
        movie_title = self.led_write.text()
        if not movie_title:
            return False

        movie = Movie(movie_title)
        result = movie.add_movies()

        if result:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)  # Attacher l'item
            self.list_movies.addItem(lw_item)

        self.led_write.setText("")

    def remove_movies(self):
        for selected_item in self.list_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_movies()
            self.list_movies.takeItem(self.list_movies.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
