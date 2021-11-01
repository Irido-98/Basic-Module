import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle('Hello World!!')

        # Set Vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label
        my_label = qtw.QLabel('Pick something from the list:')
        # Change font size of label
        my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)

        # Create an combo box
        my_combo = qtw.QComboBox(self, editable=True, insertPolicy=qtw.QComboBox.InsertAtBottom)
        # Add items to the combo box
        my_combo.addItem('Cheese', 'Something')
        my_combo.addItem('Bread', 2)
        my_combo.addItem('Tomatoes', qtw.QWidget)
        my_combo.addItem('Peppers')
        my_combo.addItems(['One', 'Two', 'Three'])
        my_combo.insertItem(2, 'Third Thing')
        # Put combo box on the screen
        self.layout().addWidget(my_combo)

        # Create a button
        my_button = qtw.QPushButton('Press Me!', clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            # Add name to label
            my_label.setText(f'You Picked: {my_combo.currentText()}!')


app = qtw.QApplication([])
mw = MainWindow()

# Run the app
app.exec_()
