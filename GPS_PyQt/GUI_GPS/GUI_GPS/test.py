import pytesseract
import pyautogui
from PIL import Image

# Take a screenshot
screenshot = pyautogui.screenshot()

# Save the screenshot to a file
screenshot.save('screenshot.png')

# Load the image file into memory
image = Image.open('screenshot.png')

# Use pytesseract to extract the text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)