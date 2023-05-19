import requests

cookie = {'visit-month': 'March'}
response = requests.get('http://rahulshettyacademy.com', cookies=cookie)
print(response.history)
print(response.status_code)

se = requests.session()
se.cookies.update({'visit-month': 'April'})

res = se.get('https://httpbin.org/cookies',allow_redirects=False, cookies={'visit-year': '2022'},timeout=2)
print(res.status_code)
print(res.text)