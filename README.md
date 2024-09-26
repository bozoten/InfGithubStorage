# Infinite GitHub Storage

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
  - [Save Files to GitHub Commit Messages](#save-files-to-github-commit-messages)
  - [Retrieve Files from Commit History](#retrieve-files-from-commit-history)
- [Main Problem with My Normal Approach](#main-problem-with-my-normal-approach)
- [Circumvention for the Problem](#circumvention-for-the-problem)
  - [Handling Large Files (e.g., `highres.jpg`)](#handling-large-files)
  - [Retrieving Files from Commit History](#retrieving-files-from-commit-history)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Environment Setup](#environment-setup)
- [Usage](#usage)
  - [Saving Files to GitHub](#saving-files-to-github)
- [Example](#example)
- [High Res Setup](#Usage-and-Environment-Setup-for-High-Resolution-Implementation)
- [Important Notes](#important-notes)
- [License](#license)

---

## Features

- Save files (images, text, etc.) to GitHub by encoding them into commit messages.
- Retrieve and decode files from specific commits in the repository's history.
- Exploit GitHub's unlimited commit history to store files in a creative way.
- Handle large files by committing them in batches of 10k characters.

## How It Works

### Save Files to GitHub Commit Messages
- Files are encoded in base64 format and stored inside commit messages.
- For large files (e.g., `highres`), the file is encoded in batches of 10k characters and committed to GitHub in chunks.

### Retrieve Files from Commit History
- You can specify a commit in the history, decode the commit message, and retrieve the original file.
- For large files stored in batches (e.g., `highres`), the script retrieves all relevant commits, concatenates the base64-encoded chunks in ascending order, and decodes the combined data back into the original file.

## Main Problem with My Normal Approach
- **GitHub Commit Message Character Limit**: 
  Each commit message on GitHub is limited to approximately a maximum of 10,000 characters. This means that larger files end up corrupted or face data loss.

## Proof of Concept:
<a href="https://github.com/bozoten/Inf-POC.git">Github Repo to the file storage repo</a>
  
<div style="display: flex; align-items: center;">
  <p>
    Normal Approach
    <div style="display: flex; align-items: center;">
    <img src="https://github.com/bozoten/InfGithubStorage/blob/master/Target_Files/highres.jpg" width="70" alt="Spiderman"/>
    <span>-></span>
    <img src="https://github.com/bozoten/InfGithubStorage/blob/master/Decoded_Targets/highResAttempt1.jpg" width="70" alt="Spiderman"/>
    </div>
  </p>

  <p>
    Circumvention
    <div style="display: flex; align-items: center;">
    <img src="https://github.com/bozoten/InfGithubStorage/blob/master/Target_Files/highres.jpg" width="70" alt="Spiderman"/>
    <span>-></span>
    <img src="https://github.com/bozoten/InfGithubStorage/blob/master/Decoded_Targets/output_image.jpg" width="70" alt="Spiderman"/>
    </div>
  </p>
</div>
  

## Circumvention for the Problem

### Handling Large Files 
For files that are too large to fit into a single commit (due to GitHub’s 10k character limit), the file is split into 10k character batches. Each batch is encoded and committed separately. The process is as follows:

1. The target file is read and encoded into base64.
2. The base64 string is split into chunks of 10,000 characters.
3. Each chunk is committed as a separate commit message.
4. When retrieving the file, all relevant commits are retrieved in ascending order, concatenated, decoded back into binary, and saved as the original file.

### Retrieving Files from Commit History
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
pip install PyGithub
```

### Environment Setup
1. Clone this repository.
2. Get your PAT or personal access token from your settings. Click on your profile photo on the right -> Open settings -> Scroll down on the left and open Developer settings -> Create a fine-grained token with permissions to your repo.
3. Add your PAT or personal access token to your encoder and decoder files:

   ```python
   token = "YOUR_PAT"
   ```

4. Replace `repo_name` in the code with your GitHub repository, formatted as `username/repo`.

## Usage

### Saving Files to GitHub
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

## Example

```bash
python encoder.py
```

After running the script, you should see messages like:

```
New File Added kiss kiss # if you add a file to an existing repo
File Upload Done Successfully. Heck yeah! # if you upload your first file to a new repo
```

Then Decode your desired file
```bash
python decoder.py
```

After running the script, you should see messages like:
```
File saved as 0decoded_files.png
```
## Usage and Environment Setup for High-Resolution Implementation

### Environment Setup

1. **Install Required Libraries**:
   Ensure you have the following Python libraries installed. You can use `pip` to install them:

   ```bash
   pip install PyGithub
   ```

2. **GitHub Personal Access Token (PAT)**:
   - Create a GitHub personal access token with appropriate permissions to access your repositories.
   - Store the token securely and replace `YOUR_PAT` in the scripts with your actual token.

### Usage Instructions

#### Encoding High-Resolution Files

1. Place the high-resolution file (e.g., `highres.jpg`) you want to encode in the same directory as `highResEncoder.py`.
2. Update the `target_path` variable in `highResEncoder.py` to match your file name.
3. Run the encoder script:

   ```bash
   python highResEncoder.py
   ```

#### Decoding High-Resolution Files

1. Execute the `highResDecoder.py` script to retrieve and decode the stored high-resolution file:

   ```bash
   python highResDecoder.py
   ```

### Notes

- Ensure your repository structure is correctly set up to avoid path issues.
- The encoding process may take some time, especially for larger files. Please be patient during execution.

## Important Notes
- **This is purely a meme project**. Do not use this for serious or large-scale storage purposes.
- The storage capacity is unlimited theoretically.
- You might want to tweak the commit size limits and GitHub API requests to optimize performance for larger files.

## License
InfGithubStorage is released under the MIT license. You can find the complete text in the file LICENSE.
