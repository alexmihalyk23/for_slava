import cv2
import pytesseract
import pyautogui
import numpy as np
from PIL import ImageGrab
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# print(pytesseract.image_to_string(Image.open('test.png')))
while True:
    img = ImageGrab.grab(bbox=(865, 150, 1920, 700))  # x, y, w, h
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    print(pytesseract.image_to_string(frame))
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0Xff == ord('q'):
        break

cv2.destroyAllWindows()