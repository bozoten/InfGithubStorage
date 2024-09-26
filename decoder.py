import base64
from github import Github

# Personal access Token
token = "YOUR_PAT"
g = Github(token)

# Repo
repo_name = "bozoten/GitSpell"
repo = g.get_repo(repo_name)

# get all commits
commits = repo.get_commits()

# specify the commit number u want in [2:3] this makes it get only the third file (its in descending order from the latest commit)
# if u need a batch just make it iterate from the commit number to the commit number u want it to be :) 
for count, commit in enumerate(commits[2:3]):
    # decodes the commit message
    decoded_data = base64.b64decode(commit.commit.message)
    # specify the extension for ur file
    file_path = str(count) + "decoded_files" + ".png"

    # write the decoded data to a file
    with open(file_path, 'wb') as file:
        file.write(decoded_data)

    print(f"File saved as {file_path}")    

