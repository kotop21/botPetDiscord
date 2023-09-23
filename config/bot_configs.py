import os
from dotenv import load_dotenv
load_dotenv()

class config:
    prefix = "$"
    TOKEN = os.getenv('TOKEN')