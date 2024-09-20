import pytesseract
from PIL import Image

def main():
    image = Image.open("./teste.png")
    text = pytesseract.image_to_string(image)
    print(text)
    return

if __name__ == "__main__":
    main()
