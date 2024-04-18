# =========================================================================
# Created with: Python v3.11.1
# Created on:   14/06/2023 14:00
# Created by:   André Henrique
# Organization: 
# Filename:     Mudança de Boot - Windowns dual boot
# Versão:       1.0.0.6
# ==========================================================================

# =========================================================================
# Importando Módulos
# =========================================================================
import sys
import os
import shutil
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox,
                               QSpacerItem, QSizePolicy)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt
import time
import json
import logging

logging.basicConfig(filename='logs/mudarboot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# =========================================================================
# Criando variáveis
# =========================================================================

with open('config/variaveis.json', 'r') as f:
    variaveis = json.load(f)

boot1 = variaveis["boot1"]
identificador1 = variaveis["identificador1"]
boot2 = variaveis["boot2"]
identificador2 = variaveis["identificador2"]

sair = "Sair"

# =========================================================================
# Criando função
# =========================================================================


def selecionar_sistema(boot_sitema):
    if boot_sitema == f"{boot1}": 
        QMessageBox.information(None, "SISTEMA SELECIONADO", f"Você selecionou o sistema: {boot1}"
                                                             f", a máquina será reiniciada!")  # pop-up
        logging.info(f"Você selecionou o sistema: {boot1}.")
        os.system(f"bcdedit /timeout 0")
        os.system(f"bcdedit /default {identificador1}")
        time.sleep(1)
        os.system(f"shutdown /r /t 0 /f")

    elif boot_sitema == f"{boot2}": 
        QMessageBox.information(None, "SISTEMA SELECIONADO", f"Você selecionou o sistema: {boot2},"
                                                             f" a máquina será reiniciada!")  # pop-up
        logging.info(f"Você selecionou o sistema: {boot2}")
        os.system(f"bcdedit /timeout 0")
        os.system(f"bcdedit /default {identificador2}")
        time.sleep(1)
        os.system(f"shutdown /r /t 0 /f")

    else:
        QMessageBox.information(None, "MÓDULO SELECIONADO: ", f"Você selecionou: {sair}")  # pop-up
        app.quit()
        return


# =========================================================================
# Janela - PySide6
# =========================================================================


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SELECIONAR BOOT")
        self.setWindowIcon(QIcon(r"image\logo_boti.ico"))
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setAlignment(Qt.AlignCenter)

        imagem_label = QLabel(self)
        imagem_pixmap = QPixmap(r"image\Windows_icon.ico")
        imagem_label.setPixmap(imagem_pixmap)
        imagem_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(imagem_label)
        titulo = QLabel("Selecione o Boot desejado: ", self)
        layout.addWidget(titulo)

        # =========================================================================
        # Botões
        # =========================================================================

        layout.addSpacing(20)
        botao1 = QPushButton(f"{boot1}", self)
        botao1.clicked.connect(lambda: selecionar_sistema(f"{boot1}"))
        botao1.setStyleSheet("background-color: CadetBlue ; color: white;")
        layout.addWidget(botao1)

        botao2 = QPushButton(f"{boot2}", self)
        botao2.clicked.connect(lambda: selecionar_sistema(f"{boot2}"))
        botao2.setStyleSheet("background-color: CadetBlue ; color: white;")
        layout.addWidget(botao2)

        botao3 = QPushButton("Sair", self)
        botao3.clicked.connect(lambda: selecionar_sistema("Sair"))
        botao3.setStyleSheet("background-color: Brown ; color: white;")
        layout.addWidget(botao3)

        self.setGeometry(400, 153, 300, 300)
        self.setFixedSize(300, 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # app.setStyle('Windows')
    window.show()
    sys.exit(app.exec())
