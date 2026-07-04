# Image Text Recognition

A simple OCR pipeline that extracts text from images using OpenCV and Tesseract, built with Python as part of the DecodeLabs internship program.

## What it does

- Loads an image and preprocesses it (grayscale, blur, thresholding)
- Runs Tesseract OCR to extract text
- Filters results to keep only words with 80% or higher confidence
- Displays recognized text and average confidence on the console
- Saves an annotated image with bounding boxes around recognized text

## How to run

```
python Image_Text_Recognition.py [path to any image]
```

## What I used

- Python 3
- OpenCV (cv2)
- pytesseract
- numpy

## Setup

### 1. Install Python packages

```
pip install -r requirements.txt
```

### 2. Install Tesseract OCR (Windows)

1. Download the installer from https://github.com/UB-Mannheim/tesseract/wiki
2. Run `tesseract-ocr-w64-setup-x.x.x.exe`
3. Install to `C:\Program Files\Tesseract-OCR`

## Project Info

DecodeLabs - Artificial Intelligence Project 4
