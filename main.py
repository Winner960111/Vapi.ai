from vapi_python import Vapi
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
assistant_id = os.getenv('ASSISTANT_ID')
vapi = Vapi(api_key=api_key) # my public API key

vapi.start(assistant_id=assistant_id) # your-assistant-id