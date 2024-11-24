from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.messages import HumanMessage
import io
import base64
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    api_key = GOOGLE_API_KEY
)

def object_detection(image):
    
    try:

        image_bytes = io.BytesIO()
        image.save(image_bytes, format='PNG')
        encoded_image = base64.b64encode(image_bytes.getvalue()).decode()

        prompt = """
            You are an AI assistant tasked with helping visually impaired individuals navigate their surroundings.
            Analyze the given image and provide:
            1. A detailed list of all objects and obstacles detected in the scene.
            2. Safety-critical information such as sharp edges, slippery areas, or uneven surfaces.
            3. Recommendations for safe navigation paths or zones.
            4. Approximate distances and spatial relationships between detected objects (if possible).
            5. Clear safety warnings for hazards.
            6. Any other guidance or precautions relevant for moving through this space.

            Format your response into the following sections:
            - **Detected Objects and Obstacles**:
            - **Safety Warnings**:
            - **Recommended Navigation Guidance**:
        """

        message = HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": prompt
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/png;base64,{encoded_image}"
                }
            ]
        )

        response = model.invoke([message])
        return response.content

    except Exception as e:
        return f"Error: {str(e)}"


