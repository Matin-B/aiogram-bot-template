# Telegram Bot Template with aiogram v3.14.0

This repository provides a clean, reusable template for creating Telegram bots using [aiogram](https://docs.aiogram.dev/en/v3.14.0/), an asynchronous Python framework. It includes handlers for basic commands, error handling, and utility functions to help you get started quickly with a structured and scalable bot.

## Repository Structure

```
.
├── config.py
├── handlers
│   ├── error.py
│   ├── __init__.py
│   └── start.py
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
└── utils
    ├── database.py
    ├── __init__.py
    └── tools.p
```

### File and Directory Overview

1. **config.py**
   - Stores important bot configurations like the bot token (`BOT_API_TOKEN`), developer Telegram ID (`DEVELOPER_TELEGRAM_ID`), and MongoDB URI (`MONGO_URI`). Update this file with your own credentials.

2. **handlers/**
   - **start.py**: Contains the command handler for `/start`.
   - **error.py**: Handles all exceptions raised during the update process. Errors are logged and a notification is sent to the developer in Telegram (identified by `DEVELOPER_TELEGRAM_ID`).
   - **__init__.py**: Aggregates all routers from the `handlers` folder, so they can easily be imported and included in the dispatcher (`dp`).

3. **main.py**
   - The entry point for the bot. It initializes the bot and dispatcher, sets up logging, and starts polling for updates.

4. **utils/**
   - **tools.py**: Contains utility functions:
     - **`debug()`**: Triggers the Python debugger (`ipdb`) for debugging purposes.
     - **`convert_bytes(size)`**: Convert a size in bytes to a human-readable string format with appropriate units (e.g., `"1.0 KB"`).
   - **database.py**: Handles database operations for the bot using MongoDB:
     - **`add_user(user_id)`**: Adds a new user to the database if the user does not already exist.
     - **`get_user(user_id)`**: Fetches user information from the database.
   - **__init__.py**: Aggregates multiple functions, making it easier to import.

5. **requirements.txt**
   - Lists dependencies required for the bot. Make sure to install them using `pip install -r requirements.txt`.

## How to Use

### Prerequisites

- Python 3.12+
- MongoDB server running and accessible. Make sure to update `MONGO_URI` in `config.py` with your MongoDB connection details.
- Install dependencies using the command:

  ```sh
  pip install -r requirements.txt
  ```

### Important Components

- **Error Handling**: The `error.py` file sends error notifications to the developer (using `DEVELOPER_TELEGRAM_ID`). It also logs errors for better debugging. This ensures that you’re always aware when an exception occurs in the bot.
- **Utility Functions**: The utility functions help in debugging (`debug()`) and provide helpful features like converting byte sizes (`convert_bytes()`).
  - The `debug()` function utilizes `ipdb` to drop into an interactive debugger.
- **Database Integration**: The `database.py` module provides methods for interacting with a MongoDB database.
  - **Adding Users**: The `add_user(user_id)` function adds a user to the database only if they do not already exist, ensuring no duplicate entries.
  - **Fetching Users**: The `get_user(user_id)` function retrieves user information from the database.

## Features

- **Command Handling**: The `/start` command, located in `handlers/start.py`, provides a simple response to introduce users to the bot.
- **Error Notifications**: Errors that occur during processing are automatically logged and forwarded to the developer, making debugging easier.
- **Database Support**: Easily store and retrieve user data using MongoDB for managing user information.
- **Modular Design**: The structure of the project keeps the bot modular, meaning that adding new features (like new commands or message handlers) is as simple as adding a new file in the `handlers` directory and including its router in `__init__.py`.


### Example: Adding a `/info` Command
1. Create `handlers/info.py`:

   ```python
   from aiogram import Router
   from aiogram.types import Message
   from aiogram.filters import Command

   router = Router()

   @router.message(Command("info"))
   async def info_command(message: Message) -> None:
       await message.reply("This is a info message.")
   ```

2. Update `handlers/__init__.py` to include the new router:

   ```python
   from .start import router as start_router
   from .error import router as error_router
   from .info import router as info_router

   __all__ = ["start_router", "error_router", "info_router"]
   ```

3. Include it in `main.py` by importing `info` and including the router:

   ```python
   from handlers import start, error, info

   dp.include_router(info.router)
   ```

## Contributing

Feel free to fork this repository and submit pull requests if you’d like to contribute new features or improvements.

## License

This project is licensed under the GPL-3.0 license.

