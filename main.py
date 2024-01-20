from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Kalkulator Sederhana')
        self.first_number = QLineEdit()
        self.second_number = QLineEdit()
        self.labelinput1 = QLabel("Masukkan Angka 1")
        self.labelinput2 = QLabel("Masukkan Angka 2")
        self.hasil_label = QLabel("Hasil Perhitungan ")
        self.add_button = QPushButton('Tambah')
        self.subtract_button = QPushButton('Kurang')
        self.multiply_button = QPushButton('Kali')
        self.divide_button = QPushButton('Bagi')
        self.pangkat_button = QPushButton('Pangkat')
        self.modulus_button = QPushButton('Modulus')

        # Connect each button's clicked signal to the appropriate slot
        self.add_button.clicked.connect(self.add_numbers)
        self.subtract_button.clicked.connect(self.subtract_numbers)
        self.multiply_button.clicked.connect(self.multiply_numbers)
        self.divide_button.clicked.connect(self.divide_numbers)
        self.pangkat_button.clicked.connect(self.pangkat_numbers)
        self.modulus_button.clicked.connect(self.modulus_numbers)

# Create a QVBoxLayout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.labelinput1)
        layout.addWidget(self.first_number)
        layout.addWidget(self.labelinput2)
        layout.addWidget(self.second_number)
        layout.addWidget(self.add_button)
        layout.addWidget(self.subtract_button)
        layout.addWidget(self.multiply_button)
        layout.addWidget(self.divide_button)
        layout.addWidget(self.pangkat_button)
        layout.addWidget(QLabel('Angka 2 sebagai pangkat'))
        layout.addWidget(self.modulus_button)
        layout.addWidget(self.hasil_label)


# Create a QWidget, set its layout, and set it as the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


class Hitung(MainWindow):
    def __init__(self):
        super().__init__()

    def add_numbers(self):
        # Add the numbers entered by the user and display the result
        result = float(self.first_number.text()) + \
            float(self.second_number.text())
        self.hasil_label.setText(str(result))

    def subtract_numbers(self):
        # Subtract the second number from the first and display the result
        result = float(self.first_number.text()) - \
            float(self.second_number.text())
        self.hasil_label.setText(str(result))

    def multiply_numbers(self):
        # Multiply the numbers entered by the user and display the result
        result = float(self.first_number.text()) * \
            float(self.second_number.text())
        self.hasil_label.setText(str(result))

    def divide_numbers(self):
        # Divide the first number by the second and display the result
        result = float(self.first_number.text()) / \
            float(self.second_number.text())
        self.hasil_label.setText(str(result))

    def pangkat_numbers(self):
        # Calculate the first number to the power of the second number
        result = float(self.first_number.text()
                       ) ** float(self.second_number.text())
        self.hasil_label.setText(str(result))

    def modulus_numbers(self):
        # Calculate the modulus of the first number by the second number
        result = float(self.first_number.text()) % float(
            self.second_number.text())
        self.hasil_label.setText(str(result))


app = QApplication([])
window = Hitung()
window.show()
app.exec_()
