# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Converter

class Converter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Converter()
        self.ui.setupUi(self)
        self.setGeometry(200,200,800,800)
        self.ui.mulButton.clicked.connect(self.multiply_button)
        self.ui.hexButton.clicked.connect(self.hex_button)
        self.ui.binButton.clicked.connect(self.bin_button)
        self.ui.bitButton.clicked.connect(self.bit_button)
        self.counter = 1


    def multiply_button(self):
        multiplier = self.ui.multiplier.text()
        number = self.ui.numPanel.text()

        if number.isdecimal() and multiplier.isdecimal():
            result = int(number)*int(multiplier)
            self.ui.console.append('{number} * {multiplier} = {result}\n'.format(number=int(number),multiplier=int(multiplier),result=result))
        else:
            self.ui.console.append('{number} * {multiplier} not correct! \n'.format(number=number,multiplier=multiplier))


    def hex_button(self):

        label_string = self.ui.numPanel.text()

        if label_string.isdecimal():
            integer_value = int(label_string)
            hex_value = hex(integer_value)
            if self.ui.radioBigButton.isChecked():
                self.ui.console.append('int to Hex (big-endian): ' + hex_value)
            else:
                little_endian_bytes = integer_value.to_bytes((integer_value.bit_length() + 7) // 8, byteorder='little')
                self.ui.console.append('int to Hex (little-endian): ' + little_endian_bytes.hex())
        else:
            bytes_data = label_string.encode('utf-8')
            if self.ui.radioBigButton.isChecked():
                self.ui.console.append('int to Hex (big-endian): ' + bytes_data.hex())
            else:
                little_endian_bytes = bytes_data[::-1]
                little_endian_hex = little_endian_bytes.hex()
                self.ui.console.append('int to Hex (little-endian): ' + little_endian_hex)


    def bin_button(self):
        label_string = self.ui.numPanel.text()
        if label_string.isdecimal():
            if self.ui.radioBigButton.isChecked():
                self.ui.console.append('int to Bin (big-endian): ' + bin(int(label_string)))

#                little_endian_bin = int(label_string).to_bytes((int(label_string).bit_length() + 7) // 8, byteorder='little').hex()
#                little_endian_bytes = int(label_string).to_bytes((int(label_string).bit_length() + 7) // 8, byteorder='little')
#                self.ui.console.append('int to Bin (little-endian): ' + little_endian_bytes)

                integer_value = int(label_string)

                # Convert the integer to binary in big-endian format
                big_endian_bin = bin(integer_value)

                # Convert the integer to binary in little-endian format
                little_endian_bytes = integer_value.to_bytes((integer_value.bit_length() + 7) // 8, byteorder='little')

                print('int to Bin (big-endian):  ' + big_endian_bin)
                print('int to Bin (little-endian): ' , little_endian_bytes)

                self.ui.console.append('int to Bin (big-endian):  ' + big_endian_bin)
#                self.ui.console.append('int to Bin (little-endian): ' + little_endian_bytes)

            else:
#                little_endian_bin = integer_value.to_bytes((integer_value.bit_length() + 7) // 8, byteorder='little').hex()

                pass



        else:
            if self.ui.radioBigButton.isChecked():
                bin_result = ''.join(format(i,'08b') for i in bytearray(label_string,'utf-8'))
                self.ui.console.append('Str to Bin (big-endian): ' + bin_result)

                little_endian_bin_result = ''.join(bin_result[i:i+8] for i in range(len(bin_result)-8, -8, -8))


                # Print the bytes in little-endian hexadecimal representation
                self.ui.console.append('String in Little-endian bytes: ' + little_endian_bin_result)



    def bit_button(self):
        label_string = self.ui.numPanel.text()

        binary_string = format(int(label_string), 'b')

        print('Двоичная строка:', binary_string)

        binary_string_big_endian = format(int(label_string), '>b')

        print('Двоичная строка (big-endian):', binary_string_big_endian)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Converter()
    widget.show()
    sys.exit(app.exec())
