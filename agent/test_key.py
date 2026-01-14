from google import genai

# REPLACE THE STRING BELOW WITH YOUR ACTUAL KEY FROM AI STUDIO
client = genai.Client(api_key="AIzaSyCchY6I2kWz3DQ3GMTX6nLrBevMkuvk9lY") 

response = client.models.generate_content(model="gemini-2.0-flash", contents="Hello")
print(response.text)