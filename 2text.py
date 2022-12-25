"""
A python program that converts an image to text. and copies the text to clipboard by a button click.

Use some GUI?

"""
import pyperclip
from PIL import Image
import pytesseract
import sys
import os
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QBuffer
from PyQt5.QtGui import QImage
from io import BytesIO


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.setWindowTitle("File Uploader")
        self.setStyleSheet("QMainWindow {background-color: #212121;}")

        # Create the main widget and set its layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create the title label and add it to the layout
        title_label = QLabel("File Uploader")
        title_label.setStyleSheet("QLabel {font-size: 24px; color: white;}")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()

        # Create the "Upload File" button
        self.upload_button = QPushButton("Upload File", self)
        self.upload_button.clicked.connect(self.upload_file)
        self.upload_button.setFixedSize(200, 50)
        button_layout.addWidget(self.upload_button)

        # Create the "Upload Clipboard" button
        self.upload_clipboard_button = QPushButton("Upload Clipboard", self)
        self.upload_clipboard_button.clicked.connect(self.upload_clipboard)
        self.upload_clipboard_button.setFixedSize(200, 50)
        button_layout.addWidget(self.upload_clipboard_button)

        # Create the "Continue" button
        self.continue_button = QPushButton("Continue", self)
        self.continue_button.clicked.connect(self.main_function)
        self.continue_button.setFixedSize(200, 50)
        button_layout.addWidget(self.continue_button)

        # Add the horizontal layout to the main layout
        layout.addLayout(button_layout)

    def upload_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        # Set the file filter to only accept certain image file types
        file_filter = "Images (*.png *.xpm *.jpg *.bmp);;PDF Files (*.pdf);;SVG Files (*.svg)"

        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select File", "", file_filter, options=options)
        if file_name:
            # Check the file extension
            _, file_extension = os.path.splitext(file_name)
            if file_extension in [".png", ".xpm", ".jpg", ".bmp", ".pdf", ".svg", ".jpeg"]:
                # Save the file name to a class attribute so it can be accessed later
                self.file_name = file_name

                # Show a message box indicating that the file was successfully uploaded
                QMessageBox.information(
                    self, "File Uploaded", "The file has been uploaded successfully.")
            else:
                # Show an error message if the file type is not supported
                QMessageBox.critical(
                    self, "Error", "This file format is not supported.")
        else:
            # Show an error message if no file was selected
            QMessageBox.critical(self, "Error", "No file was selected.")

    def upload_clipboard(self):
        # Get the image from the clipboard
        clipboard = QApplication.clipboard()
        image = clipboard.image()

        if not image.isNull():
            # Save the image to a class attribute so it can be accessed later
            self.image = image

            # Show a message box indicating that the image was successfully uploaded
            QMessageBox.information(
                self, "Image Uploaded", "The image has been uploaded successfully.")
        else:
            # Show an error message if the clipboard does not contain an image
            QMessageBox.critical(
                self, "Error", "The clipboard does not contain an image.")

    def main_function(self):
        # Check if a file or image has been selected
        if hasattr(self, "file_name"):
            # Call the main function using the file name
            main(self.file_name)
        elif hasattr(self, "image"):
            # Call the main function using the image
            main(self.image)
        else:
            print("No file or image selected")

def main(filename):
    # load the image
    image = read_image(filename)

    # get text from image
    text = convert_to_text(image)
    print("Text from image: ")
    print(text)

    # copy to the user's clipboard
    copy_to_clipboard(text)

def read_image(filename):
    if isinstance(filename, QImage):
        # Create a QBuffer object and write the image data to it
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        filename.save(buffer, "PNG")

        # Create a BytesIO object from the QBuffer
        bytes_io = BytesIO(buffer.data())

        # Close the QBuffer
        buffer.close()

        # Use the BytesIO object as the file
        return Image.open(bytes_io)
    else:
        return Image.open(filename)


def convert_to_text(image):
    return pytesseract.image_to_string(image)


def copy_to_clipboard(text):
    print("Text copied to clipboard!")
    pyperclip.copy(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
