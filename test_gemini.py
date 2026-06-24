import google.generativeai as genai

genai.configure(
    api_key="PASTE_YOUR_API_KEY_HERE"
)

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content(
    "Explain supervised learning in one sentence."
)

print(response.text)