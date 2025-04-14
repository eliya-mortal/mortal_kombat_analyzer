# Python Telegram Bot

A simple Python Telegram bot with basic command handling and message response capabilities. The bot is capable of responding to basic commands like `/start` and `/help`, as well as recognizing conversational patterns like greetings, farewells, and thanks.

## Features

- Responds to basic commands (`/start`, `/help`)
- Has simple conversations with users
- Recognizes and responds to greetings, farewells, and thanks
- Web interface to display bot status and configuration
- Easy to extend with additional commands and responses

## Project Structure

- `main.py` - Main entry point, starts both the bot and web server
- `bot.py` - Core bot functionality and setup
- `handlers.py` - Command and message handler implementations
- `config.py` - Configuration settings and environment variables
- `constants.py` - Predefined messages and response patterns
- `keep_alive.py` - Flask web server to keep the bot alive on Replit
- `templates/index.html` - Web interface template

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- A Telegram Bot Token (get one from [@BotFather](https://t.me/botfather) on Telegram)

### Configuration

1. Set up your Telegram Bot token as an environment variable:
   ```
   TELEGRAM_TOKEN=your_telegram_bot_token_here
   ```

2. Run the bot:
   ```
   python main.py
   ```

## How to Get a Telegram Bot Token

1. Open Telegram and search for the BotFather (@BotFather)
2. Start a chat and send the command `/newbot`
3. Follow the instructions to name your bot
4. Once created, BotFather will provide you with a token
5. Add this token as the `TELEGRAM_TOKEN` environment variable

## Extending the Bot

### Adding New Commands

To add a new command, edit the `handlers.py` file and add a new handler function:

```python
def my_new_command(update: Dict[str, Any], bot) -> None:
    """
    Handler for the /mynewcommand command.
    
    Args:
        update: Update object from Telegram
        bot: The bot instance
    """
    message = update.get('message', {})
    chat_id = message.get('chat', {}).get('id')
    
    # Your command logic here
    
    bot.send_message(chat_id, "This is my new command response!")
```

Then register it in the `setup_bot` function in `bot.py`:

```python
bot.register_command_handler("mynewcommand", my_new_command)
```

### Adding New Response Patterns

To add new response patterns, edit the `constants.py` file with your keywords and responses:

```python
MY_KEYWORDS = ["keyword1", "keyword2", "keyword3"]
MY_RESPONSES = [
    "Response 1",
    "Response 2",
    "Response 3"
]
```

Then update the `handle_message` function in `handlers.py` to check for these keywords:

```python
if any(keyword in message_text for keyword in MY_KEYWORDS):
    response = random.choice(MY_RESPONSES)
```

## License

This project is licensed under the MIT License.