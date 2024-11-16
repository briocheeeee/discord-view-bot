````markdown
# Discord View Bot

This is a Python-based bot that uses Selenium to generate views for Discord invite links on `https://discord.me/`. You can customize the number of views and the delay between views.

## Features

- **Fast view generation**: Uses Selenium with optimizations for faster performance.
- **Customizable delay**: Adjust the time between each view to control how quickly views are generated.
- **Persistent browser instance**: The bot reuses the browser to avoid overhead, making the process faster.

## Requirements

- Python 3.6+
- Selenium
- ChromeDriver or BraveDriver (for browser automation)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/briocheeeee/discord-view-bot.git
cd discord-view-bot
```
````

### 2. Install dependencies

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

Then install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Setup ChromeDriver or BraveBrowser

Ensure that you have `ChromeDriver` or `BraveBrowser` set up correctly. You can download `ChromeDriver` from [here](https://sites.google.com/a/chromium.org/chromedriver/).

Make sure to update the `driver_path` and `brave_path` in the `bot.py` script to point to your installed `chromedriver.exe` and `brave.exe` paths.

### 4. Running the bot

To run the bot, use the following command:

```bash
python bot.py
```

It will ask you for the Discord invite URL part and the number of views you want to generate. The bot will then start generating views for the link with the configured delay.

## Usage

1. Enter the part of the Discord link after `https://discord.me/`.
2. Choose the number of views you want to generate.
3. Specify the time delay (minimum 0.1 seconds) between each view.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Disclaimer

This bot is intended for educational purposes only. Please use it responsibly and in accordance with all applicable terms of service.

```

```
