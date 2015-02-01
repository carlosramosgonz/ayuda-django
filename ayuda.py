# ayuda.py - Navegador de la documentación de Django
#
# Copyright (C) 2015 Carlos Ramos González, <carlos+git@carlosramos.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import configparser
import os
import shelve
import sys
from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt, QVariant, pyqtSlot, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from ventanaayuda import Ui_MainWindow
from directorydialog import Ui_DirectoryDialog
from bs4 import BeautifulSoup

# Ruta donde se encuentra la documentación HTML de Django
#DOCS_PATH = '/Users/carlos/Downloads/django-docs-1/'

INDEX_FILENAME = 'genindex.html'

CACHE_PATH = '~/.django-index-cache'
CONFIG_PATH = '~/.djangohelpviewer.conf'
_docs_path = None


def get_docs_path_from_config():
    global _docs_path
    if _docs_path:
        return _docs_path

    config = configparser.ConfigParser()
    if config.read(os.path.expanduser(CONFIG_PATH)):
        if 'general' in config and 'DjangoDocsDir' in config['general']:
            _docs_path = config['general']['DjangoDocsDir']
            return _docs_path

    return None


def save_docs_path_to_config(docs_path):
    global _docs_path
    _docs_path = docs_path

    config = configparser.ConfigParser()
    config['general'] = {'DjangoDocsDir': docs_path}
    with open(os.path.expanduser(CONFIG_PATH), 'w') as configfile:
        config.write(configfile)


class DirectoryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DirectoryDialog()
        self.ui.setupUi(self)

    @property
    def docs_path(self):
        return self.ui.directoryEdit.text()

    @pyqtSlot()
    def on_openButton_clicked(self):
        filename = QFileDialog.getExistingDirectory(self, "Abrir directorio", os.path.expanduser('~'))
        self.ui.directoryEdit.setText(filename)


def get_docs_path():
    return _docs_path


def get_index_from_cache():
    """Devuelve el diccionario del índice de la caché, o None si la caché no ha
       sido creada.
    """
    cache_fullpath = os.path.expanduser(CACHE_PATH)
    with shelve.open(cache_fullpath) as db:
        if 'index-dict' not in db:
            return None
        else:
            return db['index-dict']


def save_to_cache(index_dict):
    """Guardar el diccionario en la caché."""
    cache_fullpath = os.path.expanduser(CACHE_PATH)
    with shelve.open(cache_fullpath) as db:
        db['index-dict'] = index_dict


def leer_indice():
    """Lee el fichero genindex.html de la documentación de Django y obtiene
       la lista de métodos/clases/etc y URLs.

    Devuelve un diccionario.
    """

    path = os.path.join(get_docs_path(), INDEX_FILENAME)

    soup = BeautifulSoup(open(path))
    index = {}

    tables = soup.find_all('table')
    for table in tables:
        if 'genindextable' not in table['class']:
            break
        words = table.find_all('dt')

        while len(words):
            dt = words.pop(0)
            if dt.a:
                index[dt.a.text] = dt.a['href']
            else:
                dt2 = words.pop(0)
                index[dt.text.strip()] = dt2.a['href']

    return index


def get_realhref(rel_href):
    finalpath = os.path.join(get_docs_path(), rel_href)
    return 'file://' + finalpath


class IndiceModel(QAbstractListModel):
    def __init__(self, parent=None, items={}):
        super().__init__(parent)
        self.items = items
        self.titles = sorted(items.keys())
        self.filtered_titles = None

    def filter_titles(self, word):
        if len(word) == 0:
            self.filtered_titles = None
        else:
            self.filtered_titles = tuple(title for title in self.titles if title.startswith(word))

    def rowCount(self, parent=QModelIndex()):
        if self.filtered_titles != None:
            return len(self.filtered_titles)
        else:
            return len(self.titles)

    def data(self, index, role=Qt.DisplayRole):
        current = self.filtered_titles if self.filtered_titles != None else self.titles
        if role == Qt.DisplayRole:
            return QVariant(current[index.row()])
        else:
            return QVariant()

    def get_rel_href(self, index):
        current = self.filtered_titles if self.filtered_titles != None else self.titles
        return self.items[current[index]]


class AyudaWindow(QMainWindow):
    def __init__(self, parent=None, indice_model=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        if indice_model:
            self.ui.listView.setModel(indice_model)

    @pyqtSlot(QModelIndex)
    def on_listView_clicked(self, index):
        model = self.ui.listView.model()
        url_str = get_realhref(model.get_rel_href(index.row()))
        self.ui.webView.setUrl(QUrl(url_str))

    @pyqtSlot(str)
    def on_indexSearchEdit_textChanged(self, text):
        self.ui.listView.model().filter_titles(text)
        self.ui.listView.reset()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    docs_path = get_docs_path_from_config()
    if not docs_path:
        directory_dialog = DirectoryDialog()
        result = directory_dialog.exec_()
        if result:
            docs_path = directory_dialog.docs_path
            save_docs_path_to_config(docs_path)
        else:
            print("El usuario no dado un directorio. Saliendo")
            sys.exit(-1)

    dict_index = get_index_from_cache()
    # Si el dic. no está en caché, crearlo y guardarlo
    if not dict_index:
        dict_index = leer_indice()
        save_to_cache(dict_index)
    indice_model = IndiceModel(items=dict_index)
    ayuda_window = AyudaWindow(indice_model=indice_model)
    ayuda_window.show()
    sys.exit(app.exec_())
