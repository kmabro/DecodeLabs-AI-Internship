"""
Project 4: Image or Text Recognition (Basic) - Path 1: OCR
DecodeLabs Artificial Intelligence Internship 2026
"""

import cv2
import numpy as np
import pytesseract
import sys
import os

# Configure Tesseract path for Windows
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if os.path.exists(TESSERACT_PATH):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

CONFIDENCE_THRESHOLD = 80


def load_image(path):
    img = cv2.imread(path)
    if img is None:
        print(f"Error: Could not read '{path}'")
        sys.exit(1)
    return img


def preprocess(image):
    """Grayscale -> Gaussian Blur -> Adaptive Thresholding."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blurred, 0, 255,
                              cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary


def recognize_text(binary_image):
    """Run Tesseract OCR and extract high-confidence words."""
    data = pytesseract.image_to_data(
        binary_image, output_type=pytesseract.Output.DICT,
        config="--psm 6 --oem 3"
    )

    words = []
    confidences = []

    for i in range(len(data["text"])):
        word = data["text"][i].strip()
        conf = int(data["conf"][i]) if data["conf"][i] != "-1" else 0
        if not word:
            continue

        confidences.append(conf)
        if conf >= CONFIDENCE_THRESHOLD:
            words.append({
                "word": word, "confidence": conf,
                "x": data["left"][i], "y": data["top"][i],
                "w": data["width"][i], "h": data["height"][i],
            })

    avg_conf = sum(confidences) / len(confidences) if confidences else 0
    full_text = " ".join(w["word"] for w in words)
    return words, full_text, avg_conf


def annotate_image(original, words):
    """Draw green bounding boxes around recognized text."""
    annotated = original.copy()
    for w in words:
        x, y, width, height = w["x"], w["y"], w["w"], w["h"]
        if width > 0 and height > 0:
            cv2.rectangle(annotated, (x, y),
                          (x + width, y + height), (0, 255, 0), 2)
    return annotated


def run_pipeline(image_path):
    print(f"Image: {os.path.basename(image_path)}")

    original = load_image(image_path)
    binary = preprocess(original)
    words, text, avg_conf = recognize_text(binary)

    print(f"\nRecognized Text:\n{text if text else '[No high-confidence text found]'}")
    print(f"\nAverage Confidence: {avg_conf:.1f}%")

    annotated = annotate_image(original, words)
    output_path = os.path.join("output", "recognized_text_output.png")
    os.makedirs("output", exist_ok=True)
    cv2.imwrite(output_path, annotated)
    print(f"\nOutput saved to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Image_Text_Recognition.py <image_path>")
        sys.exit(1)
    run_pipeline(sys.argv[1])
