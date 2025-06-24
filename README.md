# Road to Switch 2 - Stock Checker Bot

A Python-based automated stock monitoring system that checks the availability of the Nintendo Switch 2 across multiple Spanish retailers and sends Telegram notifications when stock becomes available.

## 🎮 Features

- **Automated Stock Monitoring**: Continuously checks stock availability every 60 seconds
- **Multi-Store Support**: Monitors GAME, MediaMarkt, and El Corte Inglés (currently GAME is fully functional)
- **Telegram Notifications**: Instant alerts when stock becomes available
- **Web Scraping**: Uses BeautifulSoup to parse retailer websites
- **Configurable**: Easy setup with environment variables

## 📋 Prerequisites

- Python 3.7 or higher
- A Telegram bot token
- A Telegram chat ID

## 🚀 Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd road-to-switch-2
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root with the following content:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   TELEGRAM_CHAT_ID=your_telegram_chat_id_here
   ```

## 🔧 Configuration

### Setting up Telegram Bot

1. Create a new bot using [@BotFather](https://t.me/botfather) on Telegram
2. Get your bot token from BotFather
3. Get your chat ID by sending a message to your bot and checking the API response

### Store URLs

The bot is configured to monitor these stores (URLs can be modified in `config.py`):

- **GAME**: Nintendo Switch 2 Mario Kart World Bundle
- **MediaMarkt**: Currently configured for DualSense controller (needs updating)
- **El Corte Inglés**: Nintendo Switch 2

## 🏃‍♂️ Usage

Run the bot with:

```bash
python main.py
```

The bot will:

1. Start monitoring stock every 60 seconds
2. Print status messages to the console
3. Send Telegram notifications when stock is found

## 📁 Project Structure

```
road-to-switch-2/
├── main.py              # Main application entry point
├── scraper.py           # Web scraping functions for each store
├── notifier.py          # Telegram notification system
├── config.py            # Configuration and environment variables
├── util.py              # Utility functions
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🔍 How It Works

### Stock Checking Process

1. **GAME Store**: Looks for "comprar" (buy) buttons or cart icons
2. **MediaMarkt**: Searches for "disponible online" (available online) text
3. **El Corte Inglés**: Checks for "añadir a la cesta" (add to cart) buttons

### Notification System

When stock is detected, the bot sends a formatted message to your Telegram chat with:

- 🎉 Stock availability notification
- Direct link to the product page
- Store name

## ⚠️ Known Issues

- **MediaMarkt**: Currently blocked by CAPTCHA protection
- **El Corte Inglés**: May get stuck in loops (needs debugging)
- **GAME**: Fully functional and working

## 🛠️ Development

### Adding New Stores

To add a new store, modify `scraper.py`:

1. Add the store URL to `config.py`
2. Create a new function following the pattern: `check_[storename]_stock()`
3. Add the function call to `main.py`

### Customizing Check Intervals

Modify the schedule in `main.py`:

```python
schedule.every(60).seconds.do(job)  # Change 60 to your desired interval
```

## 📦 Dependencies

- `beautifulsoup4`: HTML parsing
- `requests`: HTTP requests
- `schedule`: Task scheduling
- `python-dotenv`: Environment variable management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## ⚡ Disclaimer

This tool is for educational purposes. Please respect the terms of service of the websites being scraped and use responsibly. The developers are not responsible for any misuse of this tool.

## 🆘 Support

If you encounter any issues:

1. Check that all dependencies are installed
2. Verify your Telegram bot configuration
3. Ensure the store URLs are still valid
4. Check the console output for error messages

---

**Happy hunting for your Nintendo Switch 2! 🎮**
