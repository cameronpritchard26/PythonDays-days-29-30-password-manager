# Password Manager

A GUI password manager built with Python and Tkinter, part of [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) (Days 29–30) on Udemy.

## Features

- **Save credentials** — Store website, email/username, and password entries to a local JSON file.
- **Search** — Look up saved credentials by website name.
- **Password generator** — Generate a secure 16-character random password using `secrets` and automatically copy it to the clipboard.
- **Default email** — Pre-fills the email field from a `.env` file so you don't have to type it every time.
- **Confirmation dialog** — Prompts you to confirm before saving.

## Screenshot

<p align="center">
  <img src="images/logo.png" alt="Password Manager Logo" width="200">
</p>

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/cameronpritchard26/PythonDays-days-29-30-password-manager.git
   cd PythonDays-days-29-30-password-manager
   ```

2. **Create and activate a virtual environment** (optional but recommended)
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**

   Create a `.env` file in the project root:
   ```
   DEFAULT_EMAIL=your_email@example.com
   ```

### Usage

```bash
python main.py
```

1. Enter a website name, email/username, and password (or click **Generate Password**).
2. Click **Add** to save the credentials.
3. Use the **Search** button to retrieve saved credentials by website name.

## Project Structure

```
├── .env                # Environment variables (DEFAULT_EMAIL)
├── .gitignore          # Includes data.json to prevent password leaks
├── images/
│   └── logo.png        # App logo displayed in the UI
├── main.py             # Application entry point
├── data.json           # Generated at runtime — stores saved credentials
└── README.md
```

## Built With

- **[Tkinter](https://docs.python.org/3/library/tkinter.html)** — GUI framework
- **[pyperclip](https://pypi.org/project/pyperclip/)** — Clipboard copy
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — `.env` file loading
- **[secrets](https://docs.python.org/3/library/secrets.html)** — Cryptographically strong random password generation
- **[json](https://docs.python.org/3/library/json.html)** — JSON file handling

## Future Improvements

- Break down the code into multiple files for better organization.
- Allow user to customize the password length.
