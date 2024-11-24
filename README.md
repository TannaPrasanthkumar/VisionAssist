VisionAssist 👁️
VisionAssist is an AI-powered application designed to help visually impaired individuals by providing scene understanding, text extraction, and text-to-speech functionalities.

Features
🔍 Describe Scene
Leverages Google Gemini AI to provide:

A list of items detected in the image with their purpose.
An overall description of the image.
Suggestions for actions or precautions for visually impaired users.
📝 Extract Text
Extracts visible text from images using the Tesseract OCR engine.

🔊 Text-to-Speech
Converts extracted text into speech using the pyttsx3 text-to-speech library.

How It Works
Upload an Image:

Drag and drop or browse an image file (JPG, JPEG, or PNG format).
Choose a Feature:

Describe Scene: Uses Google Generative AI to analyze and describe the image.
Extract Text: Extracts readable text from the image using OCR.
Text-to-Speech: Reads the extracted text aloud.
Output:

Displays the results, whether a scene description, extracted text, or audio playback.
Installation
Prerequisites
Ensure the following tools are installed:

Python 3.8+
Tesseract OCR (Download here)
Steps
Clone the Repository:

bash
Copy code
git clone https://github.com/YourUsername/VisionAssist.git  
cd VisionAssist  
Install Dependencies:

bash
Copy code
pip install -r requirements.txt  
Set Tesseract Path:
Update the path to Tesseract in the code:

python
Copy code
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  
Set Google Gemini API Key:
Replace Your API Key in the code with your valid Google Gemini API key.

Usage
Run the application:

bash
Copy code
streamlit run app.py  
Open the application in your browser:

Navigate to http://localhost:8501.
Interact with the application:

Upload an image and select a feature to process the image.
Technologies Used
Streamlit: Interactive web application framework.
Tesseract OCR: Optical Character Recognition engine.
Google Gemini API: Advanced AI model for scene understanding.
Pyttsx3: Text-to-speech conversion library.
Screenshots
Main Interface:

Scene Description:

Extracted Text:

Credits
Developed by MD Tahseen Equbal | Built with ❤️ using Streamlit

License
This project is licensed under the MIT License.

Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request.

Let me know if you'd like additional sections, edits, or customizations!






