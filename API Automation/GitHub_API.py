# Example for Authentication
import requests
from Utilities.configurations import *

se = requests.session()
se.auth  = auth=('ababab',getPass())

url_gitHub = "https://api.github.com/user"
git_response = requests.get(url_gitHub,auth=('dshfasjf',getPass()))
print(git_response.status_code)

url2_gitHub = "https://api.github.com/user/repos"
git2_response = se.get(url2_gitHub)
print(git2_response.status_code)