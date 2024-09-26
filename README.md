# Infinite GitHub Storage

This is a meme project that enables **infinite storage** by exploiting GitHub's commit history. The script stores files encoded in base64 within commit messages, allowing you to save and retrieve files from the Git history.

## Features

- Save files (images, text, etc.) to GitHub by encoding them into commit messages.
- Retrieve and decode files from specific commits in the repository's history.
- Exploit GitHub's unlimited commit history to store files in a creative way.
- Handle large files by committing them in batches of 10k characters.

## How it Works

1. **Save Files to GitHub Commit Messages**:
    - Files are encoded in base64 format and stored inside commit messages.
    - The script checks if the file already exists in the repository, updates it if it does, and creates it if it doesn’t.
    - For large files (e.g., `highres`), the file is encoded in batches of 10k characters and committed to GitHub in chunks.
  
2. **Retrieve Files from Commit History**:
    - You can specify a commit in the history, decode the commit message, and retrieve the original file.
    - For large files stored in batches (e.g., `highres`), the script retrieves all relevant commits, concatenates the base64-encoded chunks in ascending order, and decodes the combined data back into the original file.

## Main problem with my normal approach
- **GitHub Commit Message Character Limit**: 
  Each commit message on GitHub is limited to approximately a maximum of 10,000 characters. This means that larger files end up corrupted or face data loss.

## Circumvention for the problem
- #### Handling Large Files (e.g., `highres.jpg`)

    For files that are too large to fit into a single commit (due to GitHub’s 10k character limit), the file is split into 10k character batches. Each batch is encoded and committed separately. The process is as follows:
    
    1. The target file is read and encoded into base64.
    2. The base64 string is split into chunks of 10,000 characters.
    3. Each chunk is committed as a separate commit message.
    4. When retrieving the file, all relevant commits are retrieved in ascending order, concatenated, decoded back into binary, and saved as the original file.

- #### Retrieving Files from Commit History

    1. Specify the range of commits from which you want to extract files.
    2. The script decodes the commit messages and saves the retrieved data as files.
    3. For large files stored in chunks, all commits are retrieved, their base64-encoded parts are concatenated, and then decoded back to the original file.  

## Setup

### Prerequisites

- Python 3.x
- `PyGithub` library for interacting with GitHub API
- `python-dotenv` library to handle environment variables

You can install the necessary libraries using:

```bash
pip install PyGithub python-dotenv
```

### Environment Setup

1. Clone this repository.
2. Get your PAT or personal access token from your settings. Click on your profile photo on the right -> Open settings -> Scroll down on the left and open Developer settings -> Create a fine grained token with permissions to your repo.
3. Add your PAT or personal access token to your encoder and decoder files:

```
token = "YOUR_PAT"
```

3. Replace `repo_name` in the code with your GitHub repository, formatted as `username/repo`.

### Usage

#### Saving Files to GitHub

1. Place the file you want to upload in the same directory as the script and update the `target_path` variable with the file name.
2. Run the script to encode the file in base64 and save it in a commit message on the specified branch.

```python
# Example of encoding a file
target_path = "target.jpg"  # The file to be uploaded
repo_name = "yourusername/yourrepo"  # Your GitHub repo in username/repo format
```

```python
# Example of retrieving a file from commit history
for commit in repo.get_commits()[2:3]:  # Get a specific commit
    decoded_data = base64.b64decode(commit.commit.message)
    file_path = str(count) + "decoded_files" + ".png"
```

### Example

```bash
python encoder.py
```

After running the script, you should see messages like:

```
New File Added kiss kiss # if you add a file to an existing repo
File Upload Done Successfully. Heck yeah! # if you upload ur first file to a new repo
```

Then Decode your desired file
```bash
python decoder.py
```

After running the script, you should see messages like:
```
File saved as 0decoded_files.png
```

## Important Notes

- **This is purely a meme project**. Do not use this for serious or large-scale storage purposes.
- The storage capacity is limited by GitHub's commit history limits and your own Personal Access Token’s permissions.
- You might want to tweak the commit size limits and GitHub API requests to optimize performance for larger files.

## License

This project is for fun and educational purposes. Use at your own risk!