import os
from github import Github
import base64
from dotenv import load_dotenv

load_dotenv

# personal access token
token = "YOUR_PAT"
g = Github(token)

# target File Path
target_path = "highres.jpg"

# specify reponame owner/repo
repo_name = "bozoten/GitSpell"
repo = g.get_repo(repo_name)

# encode target file into base 64 format
with open(target_path, 'rb') as file:
    target_encode = base64.b64encode(file.read())
    target_encode = target_encode.decode()

# repo config
file_path = "./GitSpell/file.txt"
commit_message = target_encode 
branch = "main"

# repo file setup
with open(file_path, 'r') as file:
    content = file.read()

# encode content to base 64 (github expects files this way) 
content_encoded = base64.b64encode(content.encode()).decode()

try:
    # if file exists get file & update it
    repo_contents = repo.get_contents(file_path, ref=branch)
    repo.update_file(repo_contents.path, commit_message, content_encoded, repo_contents.sha, branch=branch)
    print("New File Added kiss kiss")
except:
    # if file doesn't exist create the file gahahahahahaha 
    repo.create_file(file_path, commit_message, content_encoded, branch=branch)
    print("File Upload Done Succesfully. Heck yeah!")    