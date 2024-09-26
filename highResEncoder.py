import os
from github import Github
import base64
import time

# personal access token
token = "YOUR_PAT"
g = Github(token)

# target File Path
target_path = "highres.jpg"

# specify reponame owner/repo
repo_name = "bozoten/inf-POC"
repo = g.get_repo(repo_name)

file_path = "./GitSpell/file.txt"

branch = "main"

# encode target file into base 64 format
with open(target_path, 'rb') as file:
    target_encode = base64.b64encode(file.read())
    target_encode = target_encode.decode()
    batch_size = 10000

# repo file setup
with open(file_path, 'r') as file:
    content = file.read()

# encode content to base 64 (github expects files this way) 
content_encoded = base64.b64encode(content.encode()).decode()

for i in range(0, len(target_encode), batch_size):
    batch = target_encode[i: i + batch_size]
    commit_message = batch
    try:
        # if file exists get file & update it
        repo_contents = repo.get_contents(file_path, ref=branch)
        repo.update_file(repo_contents.path, commit_message, content_encoded, repo_contents.sha, branch=branch)
        print("Upload is going charmingly :3")
    except:
        # if file doesn't exist create the file gahahahahahaha 
        repo.create_file(file_path, commit_message, content_encoded, branch=branch)
        print("Upload has started pookie bear kiss kiss")

    # IM DELAYING THIS BECAUSE I DO NOT MEAN TO CAUSE ANY PROBLEMS, THIS PROJECT IS PURELY A JOKE.
    time.sleep(10)        