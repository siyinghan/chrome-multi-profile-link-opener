import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

from main import open_chrome


class LinkInputDialog(QDialog):
    """
    A dialog window that prompts the user to enter a link.

    The window contains a QLineEdit widget for the user to enter the link and a
    QPushButton widget to submit the input. When the user submits the input, the
    link is stored as an attribute of the LinkInputDialog instance and the dialog
    is closed.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Open Chrome Profiles")
        self.setMinimumSize(300, 130)
        self.link_input = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_link)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter link:"))
        layout.addWidget(self.link_input)
        layout.addStretch(1)  # Add a stretchable empty widget
        layout.addWidget(self.submit_button)
        self.setLayout(layout)
        self.link = None

    def submit_link(self):
        """
        Retrieves the link from the QLineEdit widget and stores it as an attribute
        of the LinkInputDialog instance.

        Closes the dialog using the accept() method.
        """
        self.link = self.link_input.text()  # Store the link as an attribute
        self.accept()  # Close the dialog and set the result code to QDialog.Accepted


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = LinkInputDialog()
    if dialog.exec() == QDialog.Accepted:
        link = dialog.link
        if link is not None:
            open_chrome(link)
    sys.exit(app.exec_())
