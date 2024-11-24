from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import io
import base64
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=GOOGLE_API_KEY
)

def provide_task_assistance(image, task_type):

    try:
        image_bytes = io.BytesIO()
        image.save(image_bytes, format='PNG')
        encoded_image = base64.b64encode(image_bytes.getvalue()).decode()

        task_prompts = {
            "item_identification": """
                Task: Item Identification
                You are tasked with identifying and describing items in the uploaded image. Provide:
                1. A list of visible items, including their names and types.
                2. Key characteristics and features of each item.
                3. Relative positions and arrangements in the image.
                4. Any visible warning labels or markings.
                5. Potential uses or functions of each item.
            """,
            "label_reading": """
                Task: Label Reading
                You are tasked with extracting and analyzing labels or text from the uploaded image. Provide:
                1. Names, brands, or product types.
                2. Important warnings, instructions, or symbols.
                3. Expiration dates, batch numbers, or key identifiers.
                4. Ingredient lists or content descriptions (if visible).
                5. Instructions for usage or storage.
            """,
            "navigation_help": """
                Task: Navigation Help
                You are tasked with providing navigation assistance based on the scene in the uploaded image. Provide:
                1. Key landmarks and reference points in the image.
                2. Potential obstacles or hazards to avoid.
                3. Suggested paths or directions for safe navigation.
                4. Estimated distances between key points.
                5. Specific safety precautions or warnings.
            """,
            "daily_tasks": """
                Task: Assistance for Daily Tasks
                You are tasked with providing guidance for performing daily tasks based on the uploaded image. Provide:
                1. Clear step-by-step instructions for any visible task.
                2. Safety precautions or warnings.
                3. Locations and functions of key objects.
                4. Tips and best practices for task completion.
                5. Challenges or complexities to be aware of.
            """
        }

        prompt = task_prompts.get(task_type, task_prompts["item_identification"])

        message = HumanMessage(
            content=[
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": f"data:image/png;base64,{encoded_image}"}
            ]
        )

        response = model.invoke([message])
        return response.content

    except Exception as e:
        return f"Error: {str(e)}"
