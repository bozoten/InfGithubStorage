import os
from github import Github
import base64
from dotenv import load_dotenv

load_dotenv

token = "Your_api_key"
g = Github(token)

file_path = "target.txt"

repo_name = "bozoten/GitSpell"
repo = g.get_repo(repo_name)

with open(file_path, 'rb') as file:
    encodedData = base64.b64encode(file.read())
    encodedData = encodedData.decode()
print(encodedData)