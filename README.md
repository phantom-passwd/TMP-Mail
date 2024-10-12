# TempMailGEN 📧

A Python module for generating temporary email addresses and fetching emails using Selenium and requests. This module can be used to extract important links , useful for services like Steam.

[###############¤¤¤¤¤] 70 % end

## Features ✨
- Generate temporary email addresses.
- Fetch emails and parse them for relevant information.
- Easily configurable via a JSON configuration file.

## Installation 📦

1. Clone the repository:
    ```bash
    git clone https://github.com/phantom-passwd/TMP-Mail.git
    cd TMP-Mail
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration ⚙️

Create a `config.json` file in the root directory with the following content (or just modify the one in the repo):
```json
{
  "refresh":10,    // time between message check 
  "store":false    // coming soon...
}
