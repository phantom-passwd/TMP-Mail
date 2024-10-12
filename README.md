# TempMailGEN 📧

A Python module for generating temporary email addresses and fetching emails using Selenium and requests. This module can be used to extract important links from email messages, particularly useful for services like Steam.

## Features ✨
- Generate temporary email addresses.
- Fetch emails and parse them for relevant information.
- Easily configurable via a JSON configuration file.

## Installation 📦

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/temp-mail-gen.git
    cd temp-mail-gen
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
    "browser": "chrome" // Specify the browser you want to use
}
