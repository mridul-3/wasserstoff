import pytesseract
from PIL import Image

def extract_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    image_path = 'data/segmented_objects/object_0.png'
    text = extract_text(image_path)
    print(text)
