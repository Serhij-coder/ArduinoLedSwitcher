import  sys
from PySide6.QtWidgets import  QApplication, QMainWindow
from ui_main import  Ui_MainWindow
import serial
import serial.tools.list_ports

Serial = serial.Serial()
Serial.close()
class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.onoff.setCheckable(True)

        self.ui.conect.clicked.connect(self.handle_connect_button)
        self.ui.diskonect.clicked.connect(self.handle_disconnect_button)
        self.ui.onoff.clicked.connect(self.on_off)

        available_ports = serial.tools.list_ports.comports()
        for port in available_ports:
            available_ports = [port.device]
            self.ui.port.addItems(available_ports)

        available_speeds = ["300", "600", "1200", "2400", "4800", "9600", "14400", "19200", "28800", "31250", "38400", "57600", "115200"]
        self.ui.speed.addItems(available_speeds)


    def handle_connect_button(self):
        # Ця функція буде викликатися при натисканні кнопки "conect"
        # Виконайте дії, пов'язані з підключенням
        if Serial.is_open == False:
            Serial.port = self.ui.port.currentText()
            Serial.baudrate = self.ui.speed.currentText()
            Serial.open()

    def handle_disconnect_button(self):
        # Ця функція буде викликатися при натисканні кнопки "diskonect"
        if Serial.is_open:
            Serial.close()

    def on_off(self):
        if self.ui.onoff.isChecked():
            Serial.write(b'e')
        else:
            Serial.write(b'd')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()

    sys.exit(app.exec())