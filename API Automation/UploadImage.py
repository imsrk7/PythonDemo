import requests
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('E:\\Image\\image\\1.jpg', 'rb')}
r = requests.post(url,files=files)
print(r.status_code)
print(r.text)