import sys


from PySide6.QtWidgets import QApplication
from infra.configs.connection import DBConnectionHandler
from view.tela_principal import MainWindow

db = DBConnectionHandler()
db.connect()
db.create_table_cliente()
db.close_connection()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()