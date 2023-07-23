from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QFileDialog

from gsfm_ui import Ui_MainWindow
import os,thedll,FixLib
from base64 import b64decode

gl = glt = None

if not os.path.exists('SDL2.dll'):      # 释放dll
    def get_dll(pic_code, pic_name):
        tdll = open(pic_name, 'wb')
        tdll.write(b64decode(pic_code))
        tdll.close()

    get_dll(thedll.SDL2_dll, 'SDL2.dll')

class MainWindow(QMainWindow):      #主界面
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.s_game.clicked.connect(self.fff)
        self.ui.run_b.clicked.connect(self.rb)
        self.ui.run_z.clicked.connect(self.rz)
        self.ui.jcyj.clicked.connect(self.jcyj)
        self.ui.open_f.clicked.connect(self.open_f)
        self.ui.ky.triggered.connect(self.ky)
    
    def fff(self):
        global gl,glt
        self.ui.game_list.clear()
        glt=FixLib.find()
        gl=FixLib.list_to_dict_and_list(glt)
        self.ui.game_list.addItems(gl[1])

    def rb(self):
        FixLib.backup_and_copy_sdl2_dll(gl[0][self.ui.game_list.currentText()])
        self.ui.log.showMessage(self.ui.game_list.currentText()+'被修复',5000)
    
    def jcyj(self):
        self.fff()
        if "Half-Life" in gl[0].keys():
            FixLib.backup_and_copy_sdl2_dll(gl[0]["Half-Life"])
            self.ui.log.showMessage('快速修复',5000)
        else:
            self.ui.log.showMessage('你没有 Half-Life',5000)
    
    def open_f(self):
        folder_path = QFileDialog.getExistingDirectory(self,  
                                    "选取文件夹",  
                                    "C:/")
        if folder_path:
            self.ui.game_f.setText(folder_path)
    
    def rz(self):
        if not os.path.exists(f'{self.ui.game_f.text()}\SDL2.dll'):
            FixLib.backup_and_copy_sdl2_dll(self.ui.game_f.text())
            self.ui.log.showMessage(self.ui.game_f.text()+'被修复',5000)
        else:
            self.ui.log.showMessage(self.ui.game_f.text()+'非金源引擎游戏',5000)
    
    def ky(self):
        os.system("start https://github.com/lidongxun967/GoldSrc-Fix")

if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exit(app.exec())