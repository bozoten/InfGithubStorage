import base64
from github import Github

# Specify your GitHub personal access token (make sure it's stored securely in production)
token = "YOUR_PAT"
g = Github(token)

# specify reponame owner/repo
repo_name = "bozoten/inf-POC"
repo = g.get_repo(repo_name)

# get all commits
commits = repo.get_commits()
commits_list = list(commits)

# Reverse the list of commits (reverse in-place or use slicing)
commits_list.reverse()

decode_data = ""

# Iterate over the reversed commits list
for i, commit in enumerate(commits_list):
    # Assuming you want to concatenate the commit messages for some reason
    # If you want to access a specific commit field (like the commit message or data), use commit.commit.message or similar fields
    decode_data += commit.commit.message  # or another data from the commit

# Function to decode base64 string and save it as an image
def decode_base64(base64_string, output_file_path):
    try:
        data = base64.b64decode(base64_string)

        with open(output_file_path, 'wb') as file:
            file.write(data)
        
        print(f"Image successfully saved as {output_file_path}")

    except Exception as e:
        print(f"Error decoding image: {e}")

# Attempt to decode the data and save it as an image
try:
    # Add '=' padding to the base64 string if necessary
    decode_data += "="
    decode_base64(decode_data, 'output_image.jpg')
except:
    decode_data += "=="
    decode_base64(decode_data, 'output_image.jpg')
