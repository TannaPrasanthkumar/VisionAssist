from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.messages import HumanMessage
import io
import base64
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


model = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    api_key = GOOGLE_API_KEY
)


def scene_understanding(image):
    
    try:
        # Generate detailed scene description using LangChain Vision model
        image_bytes = io.BytesIO()
        image.save(image_bytes, format='PNG')
        image_bytes = image_bytes.getvalue()

        message = HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": """
                            You are an AI assistant helping visually impaired individuals by analyzing the image. 
                            Provide:
                            1. A list of objects in the image and their possible purposes.
                            2. A detailed description of the scene, including relationships between objects or people.
                            3. Overall mood or emotion conveyed by the scene.
                            4. Recommendations for visually impaired individuals interacting with such a scene.
                        """
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/png;base64,{base64.b64encode(image_bytes).decode()}"
                }
            ]
        )

        response = model.invoke([message])
        return response.content
    
    except Exception as e:
        
        print(f"Error as {e}")