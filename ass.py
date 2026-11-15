#C:\Users\User\Desktop\Proggraming\Python\modules\WhatsApp Unknown 2026-01-19 at 16.48.19 (1).zip
from PIL import Image
import pytesseract
import os
import re

# Set path to Tesseract executable (Windows example)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Path to the folder where you extracted images
folder_path = r"C:\Users\User\Desktop\Proggraming\Python\modules\WhatsApp Unknown 2026-01-19 at 16.48.19 (1).zip"  # <-- change this to your folder

# Loop through all images in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        text = pytesseract.image_to_string(img, lang='eng')  # OCR
        # Find lines containing Q1, Q2, etc.
        question_lines = [line for line in text.split('\n') if re.search(r'\bQ\d+\b', line)]
        if question_lines:
            print(f"--- Questions in {filename} ---")
            for line in question_lines:
                print(line)
            print("\n")
