# Image to Text Converter
A python program that converts an image to text and copies the text to clipboard with a button click.

## Features
- GUI interface
- Upload image file or image from clipboard
- Convert image to text using OCR (Optical Character Recognition)
- Copy text to clipboard with a single button click

## Dependencies
- PyQt5
- PIL
- pytesseract
- pyperclip


## Installation
Run the following command to install the dependencies:
```pip install -r requirements.txt```

This will install the required packages for the program.

Note that you will still need to download and install Tesseract OCR from [here](https://github.com/UB-Mannheim/tesseract/wiki) and update the tesseract_cmd path in the code to the path of the tesseract.exe file on your system in order for the program to work correctly.

## Usage
1. Run the program with the command:
    ```python image_to_text_converter.py```

2. Click the "Upload File" button to select an image file from your system, or click the "Upload Clipboard" button to use an image that is currently in your clipboard.
3. Click the "Continue" button to convert the image to text and copy it to the clipboard.

## Notes
- The program currently only supports the following image file types: png, jpg, pdf, svg, jpeg, svg
- The program may not work correctly if the Tesseract OCR path is not set correctly.
