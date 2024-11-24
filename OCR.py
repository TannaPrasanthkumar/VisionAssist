import pytesseract
from PIL import Image
import pyttsx3

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


class ImageToSpeechConverter:
    
    def __init__(self):
        
        self.engine = pyttsx3.init()
        
    def extract_text(self, image):
        
        try:
            
            image = Image.open(image)
            text = pytesseract.image_to_string(image)
            return text.strip()
        
        except Exception as e:
            
            print(f"Error: {e}")
            
    def text_to_speech(self, text):
        
        try :
            if text:
                self.engine.say(text)
                self.engine.runAndWait()
                """tts = gTTS(text=text, lang='en')
                mp3_fp = io.BytesIO()
                tts.write_to_fp(mp3_fp)
                mp3_fp.seek(0)
                return mp3_fp.getvalue()"""
            
        except Exception as e:
            print(f"Error as {e}")
            
    def process_image(self, image):
        
        text = self.extract_text(image)
        print("Extracted text : ", text)
        
        self.text_to_speech(text)
            
if __name__ == "__main__":
    
    obj = ImageToSpeechConverter()
    
    obj.process_image("sample1.png")
    