import google.generativeai as genai
import PIL.Image

print(genai.__version__)

gemini_api_key = "AIzaSyDYfQmz7AHGbtvY4l5UJGVCa8JJgJrDjaQ"

genai.configure(api_key = gemini_api_key)
def get_response(p1,c):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([p1,c])
    return response

print("reading data")
imgs=[]
for i in range(1,4):
    imgs.append(PIL.Image.open(f'{i}.jpeg'))
size = imgs[0].size 

new_im = PIL.Image.new('RGB', (len(imgs)*size[1],(len(imgs)+1)*size[0]), (250,250,250)) 

for i in range(0,3):
    new_im.paste(imgs[i], (size[0]*(i),0)) 


img = PIL.Image.open('1.jpeg')
new_im.paste(img, (0,size[0]*(2)))
new_im.show()
responce=get_response(new_im,"if 1st image in row 2 is similar to any one image in row 1 then print intruder else no intruder")
print(responce.text)
