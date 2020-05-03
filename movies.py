import json
import os
import logging

# logging.warning("Le film est deja dans votre liste")

# Variable qui récupére le chemin d'accés au dossier actuel
CUR_DIR = os.path.dirname(__file__)
# Concaténation du CUR_DIR avec le dossier data et le fichier movies.json (.../data/movies.json)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")


def get_movies_instance():
    """
    Fonction permettant de lire data.json et de mettre tous les titres present en tant qu'instance de
    la classe Movie
    """

    with open(DATA_FILE, "r") as f:
        movies_title = json.load(f)

    """Avec comprehension de liste"""
    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies

    """Sans comprehension de liste"""
    # movies = []
    # for movie_title in movies_title:
    #    movies.append(Movie(movie_title))
    #    return print(movies)


class Movie:

    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def _get_movies(self):
        """
        Methode privée
        Methode permettant de récupérer la liste de film venant de data/movies.json
        """
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        """
        Methode privée
        Methode permettant d'ajouter des films dans data/movies.json
        """
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)

    def add_movies(self):
        """
        Methode permettant d'ajouter un film dans data/movies.json avec verification
        """
        movies = self._get_movies()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {movies} se trouve déja dans la liste")
            return False

    def remove_movies(self):
        """
        Methode permettant de supprimer des films dans data/movies.json avec vérification
        """
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            return False


# Code non executé dans le main // Phase de test
if __name__ == "__main__":
    movies = get_movies_instance()
    print(movies)