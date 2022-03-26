from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import keyboard

option = webdriver.ChromeOptions()
option.add_argument('headless')

if getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path, chrome_options=option)
else:
    driver = webdriver.Chrome(chrome_options=option)

driver.implicitly_wait(3)

driver.get('http://comci.kr:4082/th')

driver.find_element_by_id('scode').send_keys('90111')
driver.find_element_by_id('scode').send_keys(Keys.RETURN)

select = Select(driver.find_element_by_id('ba'))

select.select_by_visible_text("3-7")

tbody = driver.find_elements_by_tag_name('tbody')
tbody[1].screenshot(filename="7.png")

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('7.png')

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        self.setWindowTitle('시간표')
        self.resize(337, 369)
        self.move(0, 0)
        self.show()

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)

        self.setLayout(vbox)

    keyboard.on_press_key("Delete", lambda _:ex.setWindowOpacity(0))

    keyboard.on_press_key("End", lambda _:ex.setWindowOpacity(0.5))

    keyboard.on_press_key("Page_Down", lambda _:ex.setWindowOpacity(1))

if __name__ == '__main__':
   app = QApplication(sys.argv)
   global ex
   ex = MyApp()
   sys.exit(app.exec_())