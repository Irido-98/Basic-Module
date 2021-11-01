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
        my_label = qtw.QLabel('Type something into the box:')
        # Change font size of label
        my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)

        # Create an text box
        my_text = qtw.QTextEdit(self,
                                # plainText='This is real text!'
                                html='<h1>Big Header Text!</h1>',
                                acceptRichText=True,
                                lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                                lineWrapColumnOrWidth=50,
                                placeholderText='Type here',
                                readOnly=False
                                )

        # Put spinbox on the screen
        self.layout().addWidget(my_text)

        # Create a button
        my_button = qtw.QPushButton('Press Me!', clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            # Add name to label
            my_label.setText(f'You typed: {my_text.toPlainText()}!')
            my_text.setPlainText('You Pressed The Button!')


app = qtw.QApplication([])
mw = MainWindow()

# Run the app
app.exec_()
