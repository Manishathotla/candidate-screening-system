import os
from dotenv import load_dotenv

loaded = load_dotenv(".env")

print("Loaded:", loaded)
print("Current Folder:", os.getcwd())
print("Key:", os.getenv("GEMINI_API_KEY"))