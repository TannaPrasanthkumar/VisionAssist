# VisionAssist 👁️

VisionAssist is an AI-powered application designed to assist visually impaired individuals by providing **scene understanding**, **text extraction**, and **text-to-speech** functionalities. The application aims to enhance accessibility and independence for visually impaired users through advanced AI technologies.

---

## 🌟 Features

### 🔍 **Describe Scene**
Leverages **Google Gemini AI** to:
- Detect and list items in an image with their purpose.
- Provide an overall description of the image.
- Suggest actions or precautions for visually impaired users.

### 📝 **Extract Text**
- Extracts visible text from images using the **Tesseract OCR** engine.

### 🔊 **Text-to-Speech**
- Converts extracted text into speech using the **pyttsx3** text-to-speech library.

---

## 💡 How It Works

1. **Upload an Image**:
   - Drag and drop or browse an image file (supports JPG, JPEG, or PNG formats).

2. **Choose a Feature**:
   - **Describe Scene**: Uses **Google Generative AI** to analyze and describe the image.
   - **Extract Text**: Extracts readable text from the image using OCR.
   - **Text-to-Speech**: Reads the extracted text aloud.

3. **Output**:
   - Displays results such as scene descriptions, extracted text, or audio playback for the user.

---

## 🛠️ Installation

### Prerequisites
Make sure you have the following installed:
- **Python 3.8+**
- **Tesseract OCR** ([Download Tesseract OCR here](https://github.com/tesseract-ocr/tesseract))

### Steps to Install

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/VisionAssist.git  
   cd VisionAssist
