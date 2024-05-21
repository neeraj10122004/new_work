import google.generativeai as genai
import PIL.Image

print(genai.__version__)

gemini_api_key = #apikey

genai.configure(api_key = gemini_api_key)
def get_response(prompt,command):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([command,prompt])
    return response

for i in range(1,7):
    img = PIL.Image.open(f'{i}.jpeg')
    responce=get_response(img,"check for defects and send message defects if any defect is present else no defects")
    print(responce.text)

